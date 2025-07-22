import subprocess
from typing import Literal


class GumWrapper:
    @staticmethod
    def choose(
        choices: list[str],
        height: int | None = None,
        limit: int | None = None,
    ) -> str:
        cmd = ["gum", "choose"]
        if height is not None:
            cmd.extend(["--height", str(height)])
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
    def spin(
        title: str,
        spinner: str | None = None,
        show_output: bool = False,
        command: str = "",
    ) -> None:
        cmd = ["gum", "spin", "--title", title]
        if spinner is not None:
            cmd.extend(["--spinner", spinner])
        if show_output:
            cmd.append("--show-output")
        cmd.extend(["--", command])
        subprocess.call(cmd)

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
    def format(
        template: str | list[str] | None = None,
        theme: str | None = None,
        language: str | None = None,
        format_type: str = "markdown",
    ) -> str:
        cmd = ["gum", "format"]
        if theme is not None:
            cmd.extend(["--theme", theme])
        if language is not None:
            cmd.extend(["--language", language])
        cmd.extend(["--type", format_type])
        
        if template is not None:
            if isinstance(template, list):
                cmd.extend(template)
            else:
                cmd.append(template)
        
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def join(
        texts: list[str],
        align: str = "left",
        horizontal: bool = False,
        vertical: bool = False,
    ) -> str:
        cmd = ["gum", "join"]
        cmd.extend(["--align", align])
        if horizontal:
            cmd.append("--horizontal")
        if vertical:
            cmd.append("--vertical")
        cmd.extend(texts)
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def pager(
        content: str | None = None,
        show_line_numbers: bool = False,
        soft_wrap: bool = False,
        timeout: int | None = None,
    ) -> None:
        cmd = ["gum", "pager"]
        if show_line_numbers:
            cmd.append("--show-line-numbers")
        if soft_wrap:
            cmd.append("--soft-wrap")
        if timeout is not None:
            cmd.extend(["--timeout", str(timeout)])
        if content is not None:
            cmd.append(content)
        subprocess.call(cmd)

    @staticmethod
    def style(
        text: str | list[str] | None = None,
        foreground: str | None = None,
        background: str | None = None,
        border: str | None = None,
        border_background: str | None = None,
        border_foreground: str | None = None,
        align: str | None = None,
        height: int | None = None,
        width: int | None = None,
        margin: str | None = None,
        padding: str | None = None,
        bold: bool = False,
        faint: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
    ) -> str:
        cmd = ["gum", "style"]
        if foreground is not None:
            cmd.extend(["--foreground", foreground])
        if background is not None:
            cmd.extend(["--background", background])
        if border is not None:
            cmd.extend(["--border", border])
        if border_background is not None:
            cmd.extend(["--border-background", border_background])
        if border_foreground is not None:
            cmd.extend(["--border-foreground", border_foreground])
        if align is not None:
            cmd.extend(["--align", align])
        if height is not None:
            cmd.extend(["--height", str(height)])
        if width is not None:
            cmd.extend(["--width", str(width)])
        if margin is not None:
            cmd.extend(["--margin", margin])
        if padding is not None:
            cmd.extend(["--padding", padding])
        if bold:
            cmd.append("--bold")
        if faint:
            cmd.append("--faint")
        if italic:
            cmd.append("--italic")
        if strikethrough:
            cmd.append("--strikethrough")
        if underline:
            cmd.append("--underline")
        
        if text is not None:
            if isinstance(text, list):
                cmd.extend(text)
            else:
                cmd.append(text)
        
        return subprocess.check_output(cmd, universal_newlines=True).strip()

    @staticmethod
    def table(
        data: str | None = None,
        separator: str = ",",
        columns: list[str] | None = None,
        widths: list[int] | None = None,
        height: int = 10,
        print_static: bool = False,
        file_path: str | None = None,
        border: str = "rounded",
    ) -> str | None:
        cmd = ["gum", "table"]
        cmd.extend(["--separator", separator])
        if columns is not None:
            cmd.extend(["--columns", ",".join(columns)])
        if widths is not None:
            cmd.extend(["--widths", ",".join(map(str, widths))])
        cmd.extend(["--height", str(height)])
        if print_static:
            cmd.append("--print")
        if file_path is not None:
            cmd.extend(["--file", file_path])
        cmd.extend(["--border", border])
        
        if print_static:
            return subprocess.check_output(cmd, universal_newlines=True).strip()
        else:
            subprocess.call(cmd)
            return None

    @staticmethod
    def log(
        texts: list[str],
        file_path: str | None = None,
        format_message: bool = False,
        formatter: str = "text",
        level: str = "none",
        prefix: str | None = None,
        structured: bool = False,
        time_format: str | None = None,
    ) -> None:
        cmd = ["gum", "log"]
        if file_path is not None:
            cmd.extend(["--file", file_path])
        if format_message:
            cmd.append("--format")
        cmd.extend(["--formatter", formatter])
        cmd.extend(["--level", level])
        if prefix is not None:
            cmd.extend(["--prefix", prefix])
        if structured:
            cmd.append("--structured")
        if time_format is not None:
            cmd.extend(["--time", time_format])
        cmd.extend(texts)
        subprocess.call(cmd)

    @staticmethod
    def _call(method: str, *args, **kwargs):
        return getattr(GumWrapper, method)(*args, **kwargs)

    @staticmethod
    def _call_and_cast(method: str, cast: type, *args, **kwargs):
        return cast(GumWrapper._call(method, *args, **kwargs))


GumType = Literal["choose", "confirm", "input", "write", "filter", "spin", "file", "format", "join", "pager", "style", "table", "log"]
