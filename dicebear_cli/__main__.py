# MIT License
#
# Copyright (c) 2024 jvherck (on GitHub)
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
from string import ascii_letters, digits
from random import choices
from dicebear import *

from __init__ import __version__


@click.group()
@click.version_option(__version__, "--version", "-v")
@click.help_option("--help", "-h")
def cli(): pass


@cli.command(name="create", help="Create one or more new avatars (no customising possible through CLI).")
@click.argument("style", type=click.STRING, default=None, required=False)
# help="The style of the avatar. All styles can be found on https://avatars.dicebear.com/styles or `DStyle.list`")
@click.option("--seed", "-s", show_default=True, type=click.STRING, default=None,
              help="The string to create the avatar (USE QUOTATION MARKS IF YOU WANT A MULTIPLE WORD SEED). Every unique string has their own unique avatar.")
@click.option("--count", "-c", show_default=True, type=click.INT, default=1,
              help="The amount of avatars to make at once (they will all have the same style and seed if you add these to the command line, "
                   "leaving these options blank will create multiple random avatars.")
@click.option("--format", "-f", show_default=True, type=click.STRING, default=DFormat.svg,
              help="The format of the avatar. Get a list of all formats with `dicebear formats`.")
@click.help_option("--help", "-h")
def create(seed: str, style: str, count: int, format: str):
    avs = []
    try:
        if count > 1 and style and seed:
            click.echo("Both a style and seed have been given, generating multiple avatars just gives the same result. "
                       "(that's why only 1 is returned)")
            count = 1
        for _ in range(count):
            if seed is None:
                seed = "".join(choices(ascii_letters+digits, k=8))
            av = DAvatar(DStyle.random() if style is None else DStyle.from_str(str(style)), seed)
            if format == DFormat.svg: avs.append(av.url_svg)
            elif format == DFormat.png: avs.append(av.url_png)
            elif format == DFormat.jpg: avs.append(av.url_jpg)
            elif format == DFormat.json: avs.append(av.url_json)
            else:
                log_error(ImageError("This format is not supported. Use `dicebear formats` to see all supported formats."))
                return
    except Error as e:
        log_error(e)
        return
    for x in avs: click.echo(x)


@cli.command(name="styles", help="See a list of all available styles.")
@click.help_option("--help", "-h")
def styles():
    for s in DStyle.list: click.echo(s)

@cli.command(name="formats", help="See a list of all available formats.")
@click.help_option("--help", "-h")
def formats():
    for f in DFormat.list: click.echo(f)


if __name__ == '__main__':
    cli()
