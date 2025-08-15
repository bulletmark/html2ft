## HTML2FT - Command line tool to convert HTML to FastHTML Python FT components
[![PyPi](https://img.shields.io/pypi/v/html2ft)](https://pypi.org/project/html2ft/)

[`html2ft`][html2ft] is a command line tool to convert [HTML][html] to
[FastHTML][fasthtml] Python [FT components][fasthtml_comp]. It is a command line
implementation of the online [HTML to FastHTML](https://h2f.answer.ai/) converter.

The latest documentation and code is available at https://github.com/bulletmark/html2ft.

## Usage

Type `html2ft -h` to view the usage summary:

```
usage: html2ft [-h] [-a] [infile]

Command line tool to convert HTML to FastHTML Python FT components. Output is
written to stdout.

positional arguments:
  infile             input file (default is stdin)

options:
  -h, --help         show this help message and exit
  -a, --attrs-first  output attributes first instead of children first
```

## Installation and Upgrade

Python 3.10 or later is required. You can run [`htmt2ft`][html2ft] most easily
using [`uvx`][uvx]. Just make sure [`uv`][uv] is installed and then run the
following command which will install [`html2ft` from PyPi][html2ft_py] "on the fly" and will
then run it immediately:

```sh
$ uvx html2ft [myfile.html]
```

Or install [`html2ft`][html2ft] formally on your system using using [`uv
tool`][uvtool] (or [`pipx`][pipx] or [`pipxu`][pipxu]). To install:

```sh
$ uv tool install html2ft
```

To upgrade:

```sh
$ uv tool upgrade html2ft
```

To uninstall:

```sh
$ uv tool uninstall html2ft
```

## License

Copyright (C) 2025 Mark Blakeney. This program is distributed under the
terms of the GNU General Public License. This program is free software:
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation,
either version 3 of the License, or any later version. This program is
distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License at
<https://en.wikipedia.org/wiki/GNU_General_Public_License> for more details.

[html]: https://en.wikipedia.org/wiki/HTML
[html2ft]: https://github.com/bulletmark/html2ft
[html2ft_py]: https://pypi.org/project/html2ft
[fasthtml]: https://fastht.ml/
[fasthtml_comp]: https://www.fastht.ml/docs/explains/explaining_xt_components.html
[pipx]: https://github.com/pypa/pipx
[pipxu]: https://github.com/bulletmark/pipxu
[uv]: https://docs.astral.sh/uv/
[uvtool]: https://docs.astral.sh/uv/guides/tools/#using-tools
[uvx]: https://docs.astral.sh/uv/guides/tools/#using-tools

<!-- vim: se ai syn=markdown: -->
