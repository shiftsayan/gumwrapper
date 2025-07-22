from typing import TypedDict


class ChooseProtocol(TypedDict, total=False):
    choices: list[str]
    height: int
    limit: int


class ConfirmProtocol(TypedDict, total=False):
    message: str


class InputProtocol(TypedDict, total=False):
    prompt: str
    placeholder: str
    value: str
    password: bool
    width: int


class WriteProtocol(TypedDict, total=False):
    placeholder: str
    width: int


class FilterProtocol(TypedDict, total=False):
    items: list[str]
    placeholder: str
    limit: int


class SpinProtocol(TypedDict, total=False):
    title: str
    spinner: str
    show_output: bool
    command: str
