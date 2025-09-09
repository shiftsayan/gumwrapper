import argparse
from functools import wraps
from typing import Any, Callable

from pydantic import BaseModel

from gumwrapper.wrapper import GumPrompt, GumWrapperType

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
    password: bool | None = None
    limit: int | None = None
    path: str | None = None


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
    password: bool | None = None,
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
        choices: List of choices (for choose/filter methods)
        message: Message text (for input/confirm methods)
        placeholder: Placeholder text (for input/write/filter methods)
        password: Hide input (for input method)
        limit: Limit selections (for choose/filter methods)
        path: Starting path (for file method)
    """

    gum_argument = GumArgument(
        argument_name=name,
        argument_type=argument_type,
        gum_wrapper_type=prompt_method,
        default=default,
        required=required,
        help=help,
        message=message,
        placeholder=placeholder,
        choices=choices,
        password=password,
        limit=limit,
        path=path,
    )

    def decorator(func: Callable):
        gum_data = getattr(func, GUM_DATA_KEY, [])
        gum_data.append(gum_argument)

        @wraps(func)
        def wrapper(*args, **call_kwargs):
            if args or call_kwargs:
                # Function called with arguments, run normally
                return func(*args, **call_kwargs)
            else:
                # Function called without arguments, collect from prompts
                return _execute_with_prompts(wrapper)

        setattr(wrapper, GUM_DATA_KEY, gum_data)

        return wrapper

    return decorator


def _parse_name(name: str) -> str:
    """Parse argument name to remove leading dashes and replace with underscores."""
    return name.lstrip("-").replace("-", "_")


def _execute_with_prompts(wrapper: Callable):
    """Execute function by collecting arguments from CLI or gum prompts."""
    gum_arguments: list[GumArgument] = getattr(wrapper, GUM_DATA_KEY, [])

    if not gum_arguments:
        return wrapper()

    # Parse CLI arguments
    parser = argparse.ArgumentParser(add_help=False)
    for gum_argument in gum_arguments:
        parser.add_argument(
            f"--{gum_argument.argument_name}",
            type=gum_argument.argument_type,
            help=gum_argument.help,
        )

    parsed_args, _ = parser.parse_known_args()
    cli_args = {k: v for k, v in vars(parsed_args).items() if v is not None}

    collected_args = {}

    for gum_argument in gum_arguments:
        arg_name = _parse_name(gum_argument.argument_name)

        # Check if provided via CLI
        if gum_argument.argument_name in cli_args:
            collected_args[arg_name] = cli_args[gum_argument.argument_name]
            continue

        if gum_argument.gum_wrapper_type is None:
            collected_args[arg_name] = gum_argument.default
            continue

        # Validate parameters against allowed parameters for the method
        if gum_argument.gum_wrapper_type in PROMPT_TO_PARAMS:
            allowed_params = PROMPT_TO_PARAMS[gum_argument.gum_wrapper_type]
            provided_params = {
                k
                for k, v in {
                    "choices": gum_argument.choices,
                    "message": gum_argument.message,
                    "placeholder": gum_argument.placeholder,
                    "password": gum_argument.password,
                    "limit": gum_argument.limit,
                    "path": gum_argument.path,
                }.items()
                if v is not None
            }
            invalid_params = provided_params - allowed_params
            if invalid_params:
                raise ValueError(
                    f"Invalid parameters for {gum_argument.gum_wrapper_type}: {invalid_params}. "
                    f"Allowed parameters: {allowed_params}"
                )

        # Choose
        if gum_argument.gum_wrapper_type == "choose":
            assert gum_argument.choices
            value = GumPrompt._call_and_cast(
                "choose",
                gum_argument.argument_type,
                choices=gum_argument.choices,
                limit=gum_argument.limit,
            )
        # Filter
        elif gum_argument.gum_wrapper_type == "filter":
            assert gum_argument.choices
            value = GumPrompt._call_and_cast(
                "filter",
                gum_argument.argument_type,
                items=gum_argument.choices,
                placeholder=gum_argument.placeholder,
                limit=gum_argument.limit,
            )
        # Confirm
        elif gum_argument.gum_wrapper_type == "confirm":
            if gum_argument.message:
                message = gum_argument.message
            else:
                message = f"Please confirm {gum_argument.argument_name}"
            value = GumPrompt._call_and_cast(
                "confirm",
                gum_argument.argument_type,
                message=message,
            )
        # Input
        elif gum_argument.gum_wrapper_type == "input":
            if gum_argument.message:
                message = gum_argument.message.rstrip() + " "
            else:
                message = f"{gum_argument.argument_name} "
            value = GumPrompt._call_and_cast(
                "input",
                gum_argument.argument_type,
                prompt=message,
                placeholder=gum_argument.placeholder,
                value=(
                    str(gum_argument.default)
                    if gum_argument.default is not None
                    else None
                ),
                password=gum_argument.password,
            )
        # Write
        elif gum_argument.gum_wrapper_type == "write":
            value = GumPrompt._call_and_cast(
                "write",
                gum_argument.argument_type,
                placeholder=gum_argument.placeholder,
            )
        # File
        elif gum_argument.gum_wrapper_type == "file":
            value = GumPrompt._call_and_cast(
                "file",
                gum_argument.argument_type,
                path=gum_argument.path,
            )
        else:
            raise ValueError(f"Invalid prompt method: {gum_argument.gum_wrapper_type}")

        collected_args[arg_name] = value

    return wrapper(**collected_args)
