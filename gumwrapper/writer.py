import subprocess
from typing import Literal

GumWriterType = Literal["spin", "format", "join", "pager", "style", "table", "log"]


class GumWriter:
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
