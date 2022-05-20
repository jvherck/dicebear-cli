# MIT License
#
# Copyright (c) 2022 jvherck (https://jvherck.github.io/dicebear/)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import click
import __init__
from dicebear import *
from random import choices, choice
from string import ascii_lowercase, digits


@click.group()
@click.version_option(__init__.__version__, "--version", "-v")
def cli():
    pass


@cli.command(name="create", help="Create one or more new avatars (no customising possible through CLI).")
@click.argument("style", type=click.STRING, default=None, required=False)
# help="The style of the avatar. All styles can be found on https://avatars.dicebear.com/styles or `DStyle.list`")
@click.option("--seed", "-s", show_default=True, type=click.STRING, default=None,
              help="The string to create the avatar (USE QUOTATION MARKS IF YOU WANT A MULTIPLE WORD SEED). Every unique string has their own unique avatar.")
@click.option("--count", "-c", show_default=True, type=click.INT, default=1,
              help="The amount of avatars to make at once (they will all have the same style and seed if you add these to the command line, "
                   "leaving these options blank will create multiple random avatars.")
@click.option("--format", "-f", show_default=True, type=click.STRING, default=DFormat.png,
              help="The format of the avatar. All formats can be found on https://github.com/jvherck/dicebear#formats or `DFormat.list`")
@click.help_option("--help", "-h")
def create(seed, style: str, count: int, format: str):
    avs = []
    # rstyle = True if style is None else False
    stylelist = []
    y = 1
    while y <= count:
        stylelist.append(choice(DStyle.list))
        y += 1

    try:
        x = 1
        while x <= count:
            if count > 1 or seed is None:
                seed = "".join(choices(ascii_lowercase + digits, k=20))

            av = DAvatar(DStyle.random if style is None else DStyle.from_str(str(stylelist[x-1])), seed)

            if format == DFormat.png:
                avs.append(av.url_png)
            elif format == DFormat.svg:
                avs.append(av.url_svg)
            else:
                log_error(ImageError("This format is not supported. Check https://github.com/jvherck/dicebear-cli#styles to see all supported formats."))
                return
            x += 1
    except Error as e:
        log_error(e)
        return
    for x in avs:
        click.echo(x)


@cli.command(name="styles", help="See a list of all available styles.")
@click.help_option("--help", "-h")
def styles():
    for style in DStyle.list:
        click.echo(style)


if __name__ == '__main__':
    cli()
