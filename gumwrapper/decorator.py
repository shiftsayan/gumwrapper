import argparse
from typing import Any, Callable

from pydantic import BaseModel

from one.gum.wrapper import GumType, GumWrapper

# class GumCommand:
#     def __init__(self, name: str, func: Callable):
#         self.name = name
#         self.func = func


GUM_DATA_KEY = "__gum_data__"


class GumArgument(BaseModel):
    argument_name: str
    argument_cls: type
    prompt_method: GumType | None
    default: Any
    required: bool
    help: str | None


def argument(
    name: str,
    type: type,
    prompt_method: GumType | None = None,
    *,
    default: Any = None,
    required: bool = False,
    help: str | None = None,
):
    gum_argument = GumArgument(
        argument_name=name,
        argument_cls=type,
        prompt_method=prompt_method,
        default=default,
        required=required,
        help=help,
    )

    def decorator(func: Callable):
        gum_data = getattr(func, GUM_DATA_KEY, [])
        gum_data.append(gum_argument)
        setattr(func, GUM_DATA_KEY, gum_data)
        return func

    return decorator


def _parse_name(name: str) -> str:
    # remove leading dashes and replace with underscores
    return name.lstrip("-").replace("-", "_")


def command(
    program_name: str | None = None,
    description: str | None = None,
    epilog: str | None = None,
):
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=description,
        epilog=epilog,
    )

    def decorator(func: Callable):
        gum_arguments: list[GumArgument] = getattr(func, GUM_DATA_KEY, [])
        map_argument_name_to_gum_argument = {}

        for _gum_argument in gum_arguments:
            parser.add_argument(
                _gum_argument.argument_name,
                type=_gum_argument.argument_cls,
                # default=_gum_argument.default,
                # type=_gum_argument.argument_cls,
                # choices=
                required=_gum_argument.required,
                help=_gum_argument.help,
            )
            map_argument_name_to_gum_argument[
                _parse_name(_gum_argument.argument_name)
            ] = _gum_argument

        parsed_arguments = vars(parser.parse_args())
        for _argument, _value in parsed_arguments.items():
            if _value is None:
                gum_argument = map_argument_name_to_gum_argument[_argument]
                if gum_argument.prompt_method is not None:
                    _value = GumWrapper._call_and_cast(
                        gum_argument.prompt_method,
                        gum_argument.argument_cls,
                    )
                else:
                    raise ValueError(f"Argument {_argument} is required")
                parsed_arguments[_argument] = _value

        def wrapped_func(*args, **kwargs):
            return func(*args, **parsed_arguments, **kwargs)

        return wrapped_func

    return decorator
