#!/usr/bin/env python3
"""
Command line tool to convert HTML to FastHTML Python FT components.
Output is written to stdout.
"""

from argparse import ArgumentParser, FileType

from fasthtml.common import html2ft


def main():
    "Main code"
    opt = ArgumentParser(description=__doc__)
    opt.add_argument(
        '-a',
        '--attrs-first',
        action='store_true',
        help='output attributes first instead of children first',
    )
    opt.add_argument(
        'infile',
        nargs='?',
        type=FileType(),
        default='-',
        help='input file (default is stdin)',
    )

    args = opt.parse_args()
    print(html2ft(args.infile.read(), attr1st=args.attrs_first))


if __name__ == '__main__':
    main()
