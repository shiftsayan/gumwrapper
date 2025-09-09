import argparse
from typing import Any, Callable

from pydantic import BaseModel

from gumwrapper.wrapper import GumWrapper, GumWrapperType

GUM_DATA_KEY = "__gum_data__"


class GumArgument(BaseModel):
    argument_name: str
    argument_type: type
    gum_wrapper_type: GumWrapperType | None
    #
    default: Any
    required: bool
    help: str | None
    #
    message: str | None = None
    placeholder: str | None = None
    choices: list[str] | None = None
    password: bool = False
    limit: int | None = None


PROMPT_TO_PARAMS = {
    # Selection
    "choose": {"choices", "limit"},
    "filter": {"choices", "limit"},
    "file": {"path"},
    # Confirmation
    "confirm": {"message"},
    # Input
    "input": {"message", "placeholder", "password"},
    "write": {"placeholder"},
}


def argument(
    name: str,
    argument_type: type,
    prompt_method: GumWrapperType | None = None,
    *,
    default: Any = None,
    required: bool = False,
    help: str | None = None,
    # Direct prompt parameters (most commonly used ones)
    choices: list[str] | None = None,
    message: str | None = None,
    placeholder: str | None = None,
    password: bool = False,
    limit: int | None = None,
    path: str | None = None,
):
    """
    Decorator to define function arguments with optional gum prompts.

    Args:
        name: Argument name
        argument_type: Python type for the argument
        prompt_method: Gum command to use for prompting
        default: Default value
        required: Whether argument is required
        help: Help text
        choices: List of choices for choose/filter methods
        prompt: Prompt text (for input/confirm methods)
        placeholder: Placeholder text (for input/write/filter methods)
        message: Message text (for confirm method)
        password: Hide input (for input method)
        limit: Limit selections (for choose/filter methods)
        path: Starting path (for file method)
        **kwargs: Additional parameters (validated against method)
    """

    # Validate extra kwargs against allowed parameters for the prompt method
    if prompt_method and kwargs:
        allowed_params = PROMPT_TO_PARAMS.get(prompt_method, set())
        extra_params = set(kwargs.keys()) - allowed_params
        if extra_params:
            raise ValueError(
                f"Invalid parameters for {prompt_method}: {extra_params}. "
                f"Allowed parameters: {allowed_params}"
            )

    # Store all prompt parameters
    prompt_params = {
        "prompt": prompt,
        "placeholder": placeholder,
        "message": message,
        "password": password,
        "limit": limit,
        "height": height,
        "path": path,
        **kwargs,
    }

    # Remove None values
    prompt_params = {k: v for k, v in prompt_params.items() if v is not None}

    gum_argument = GumArgument(
        argument_name=name,
        argument_type=argument_type,
        gum_wrapper_type=prompt_method,
        default=default,
        required=required,
        help=help,
        choices=choices,
        **{k: v for k, v in prompt_params.items() if k in GumArgument.model_fields},
    )

    def decorator(func: Callable):
        gum_data = getattr(func, GUM_DATA_KEY, [])
        gum_data.append(gum_argument)
        setattr(func, GUM_DATA_KEY, gum_data)

        # Auto-execute the function if called directly
        def wrapper(*args, **call_kwargs):
            if args or call_kwargs:
                # Function called with arguments, run normally
                return func(*args, **call_kwargs)
            else:
                # Function called without arguments, collect from prompts
                return _execute_with_prompts(func)

        return wrapper

    return decorator


def _parse_name(name: str) -> str:
    """Parse argument name to remove leading dashes and replace with underscores."""
    return name.lstrip("-").replace("-", "_")


def _execute_with_prompts(func: Callable):
    """Execute function by collecting arguments from gum prompts."""
    gum_arguments: list[GumArgument] = getattr(func, GUM_DATA_KEY, [])

    if not gum_arguments:
        # No arguments defined, just call the function
        return func()

    collected_args = {}

    for gum_argument in gum_arguments:
        arg_name = _parse_name(gum_argument.argument_name)

        if gum_argument.gum_wrapper_type is None:
            if gum_argument.default is not None:
                collected_args[arg_name] = gum_argument.default
            elif gum_argument.required:
                raise ValueError(
                    f"Argument {arg_name} is required but no prompt method specified"
                )
            else:
                collected_args[arg_name] = None
            continue

        # Build kwargs for the gum method
        prompt_kwargs = {}

        # Add method-specific parameters
        if gum_argument.gum_wrapper_type == "choose":
            choices = gum_argument.choices or ["yes", "no"]
            if gum_argument.limit is not None:
                prompt_kwargs["limit"] = gum_argument.limit

            value = GumPrompt._call_and_cast(
                gum_argument.gum_wrapper_type,
                gum_argument.argument_type,
                choices,
                **prompt_kwargs,
            )

        elif gum_argument.gum_wrapper_type == "filter":
            items = gum_argument.choices or ["item1", "item2", "item3"]
            if gum_argument.placeholder is not None:
                prompt_kwargs["placeholder"] = gum_argument.placeholder
            if gum_argument.limit is not None:
                prompt_kwargs["limit"] = gum_argument.limit

            value = GumPrompt._call_and_cast(
                gum_argument.gum_wrapper_type,
                gum_argument.argument_type,
                items,
                **prompt_kwargs,
            )

        elif gum_argument.gum_wrapper_type == "confirm":
            message = (
                gum_argument.message or f"Please confirm {gum_argument.argument_name}"
            )
            result = GumPrompt._call(gum_argument.gum_wrapper_type, message)
            value = gum_argument.argument_type(result)

        elif gum_argument.gum_wrapper_type in ["input", "write"]:
            if gum_argument.prompt is not None:
                prompt_kwargs["prompt"] = gum_argument.prompt
            elif gum_argument.gum_wrapper_type == "input":
                prompt_kwargs["prompt"] = f"Enter {gum_argument.argument_name}: "

            if gum_argument.placeholder is not None:
                prompt_kwargs["placeholder"] = gum_argument.placeholder
            if gum_argument.password:
                prompt_kwargs["password"] = True

            value = GumPrompt._call_and_cast(
                gum_argument.gum_wrapper_type,
                gum_argument.argument_type,
                **prompt_kwargs,
            )

        elif gum_argument.gum_wrapper_type == "file":
            if hasattr(gum_argument, "path") and gum_argument.path is not None:
                prompt_kwargs["path"] = gum_argument.path

            value = GumPrompt._call_and_cast(
                gum_argument.gum_wrapper_type,
                gum_argument.argument_type,
                **prompt_kwargs,
            )

        else:
            # For other methods, use minimal kwargs
            value = GumPrompt._call_and_cast(
                gum_argument.gum_wrapper_type,
                gum_argument.argument_type,
                **prompt_kwargs,
            )

        collected_args[arg_name] = value

    return func(**collected_args)


def command(
    program_name: str | None = None,
    description: str | None = None,
    epilog: str | None = None,
):
    """
    Decorator to create command-line interface for a function.

    Args:
        program_name: Name of the program
        description: Description text
        epilog: Epilog text
    """

    def decorator(func: Callable):
        gum_arguments: list[GumArgument] = getattr(func, GUM_DATA_KEY, [])

        if not gum_arguments:
            # No arguments, just return the function
            return func

        parser = argparse.ArgumentParser(
            prog=program_name,
            description=description,
            epilog=epilog,
        )

        map_argument_name_to_gum_argument = {}

        for gum_argument in gum_arguments:
            parser.add_argument(
                gum_argument.argument_name,
                type=gum_argument.argument_type,
                required=gum_argument.required,
                help=gum_argument.help,
            )
            map_argument_name_to_gum_argument[
                _parse_name(gum_argument.argument_name)
            ] = gum_argument

        parsed_arguments = vars(parser.parse_args())

        for argument_name, value in parsed_arguments.items():
            if value is None:
                gum_argument = map_argument_name_to_gum_argument[argument_name]
                if gum_argument.prompt_method is not None:
                    # Same prompting logic as _execute_with_prompts
                    # (This is a bit duplicated but keeps the command decorator working)
                    if gum_argument.prompt_method == "choose":
                        choices = gum_argument.choices or ["yes", "no"]
                        prompt_kwargs = {}
                        if gum_argument.limit is not None:
                            prompt_kwargs["limit"] = gum_argument.limit
                        value = GumPrompt._call_and_cast(
                            gum_argument.prompt_method,
                            gum_argument.argument_cls,
                            choices,
                            **prompt_kwargs,
                        )
                    elif gum_argument.prompt_method == "confirm":
                        message = (
                            gum_argument.message
                            or f"Please confirm {gum_argument.argument_name}"
                        )
                        result = GumPrompt._call(gum_argument.prompt_method, message)
                        value = gum_argument.argument_cls(result)
                    elif gum_argument.prompt_method == "input":
                        prompt_kwargs = {}
                        if gum_argument.prompt is not None:
                            prompt_kwargs["prompt"] = gum_argument.prompt
                        else:
                            prompt_kwargs["prompt"] = (
                                f"Enter {gum_argument.argument_name}: "
                            )
                        if gum_argument.placeholder is not None:
                            prompt_kwargs["placeholder"] = gum_argument.placeholder
                        if gum_argument.password:
                            prompt_kwargs["password"] = True
                        value = GumPrompt._call_and_cast(
                            gum_argument.prompt_method,
                            gum_argument.argument_cls,
                            **prompt_kwargs,
                        )
                    # Add other methods as needed...
                    else:
                        value = GumPrompt._call_and_cast(
                            gum_argument.prompt_method,
                            gum_argument.argument_cls,
                        )
                else:
                    if gum_argument.required:
                        raise ValueError(f"Argument {argument_name} is required")
                    value = gum_argument.default

                parsed_arguments[argument_name] = value

        def wrapped_func(*args, **kwargs):
            return func(*args, **parsed_arguments, **kwargs)

        return wrapped_func

    return decorator
