import subprocess
from typing import Literal

GumWrapperType = Literal["choose", "confirm", "input", "write", "filter", "file"]


class GumPrompt:
    @staticmethod
    def choose(
        choices: list[str],
        limit: int | None = None,
    ) -> str:
        cmd = ["gum", "choose"]
        if limit is not None:
            cmd.extend(["--limit", str(limit)])
        cmd.extend(choices)
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def confirm(message: str) -> bool:
        cmd = ["gum", "confirm", message]
        return subprocess.call(cmd) == 0

    @staticmethod
    def input(
        prompt: str | None = None,
        placeholder: str | None = None,
        value: str | None = None,
        password: bool = False,
        width: int | None = None,
    ) -> str:
        cmd = ["gum", "input"]
        if prompt is not None:
            cmd.extend(["--prompt", prompt])
        if placeholder is not None:
            cmd.extend(["--placeholder", placeholder])
        if value is not None:
            cmd.extend(["--value", value])
        if password:
            cmd.append("--password")
        if width is not None:
            cmd.extend(["--width", str(width)])
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def write(placeholder: str | None = None, width: int | None = None) -> str:
        cmd = ["gum", "write"]
        if placeholder is not None:
            cmd.extend(["--placeholder", placeholder])
        if width is not None:
            cmd.extend(["--width", str(width)])
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def filter(
        items: list[str],
        placeholder: str | None = None,
        limit: int | None = None,
    ) -> list[str]:
        cmd = ["gum", "filter"]
        if placeholder is not None:
            cmd.extend(["--placeholder", placeholder])
        if limit is not None:
            cmd.extend(["--limit", str(limit)])
        process = subprocess.Popen(
            cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True
        )
        stdout, _ = process.communicate("\n".join(items))
        return [item.strip() for item in stdout.strip().split("\n")]

    @staticmethod
    def file(
        path: str | None = None,
        cursor: str | None = None,
        all_files: bool = False,
        file_selection: bool = True,
        directory_selection: bool = False,
        height: int | None = None,
        timeout: int | None = None,
    ) -> str:
        cmd = ["gum", "file"]
        if path is not None:
            cmd.append(path)
        if cursor is not None:
            cmd.extend(["--cursor", cursor])
        if all_files:
            cmd.append("--all")
        if file_selection:
            cmd.append("--file")
        if directory_selection:
            cmd.append("--directory")
        if height is not None:
            cmd.extend(["--height", str(height)])
        if timeout is not None:
            cmd.extend(["--timeout", str(timeout)])
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def _call(method: str, *args, **kwargs):
        return getattr(GumPrompt, method)(*args, **kwargs)

    @staticmethod
    def _call_and_cast(method: str, cast: type, *args, **kwargs):
        return cast(GumPrompt._call(method, *args, **kwargs))
