import argparse

from piecash_qif_import import import_qif


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-v', '--verbose', help='Verbose (debug) logging', action='store_true')
    parser.add_argument('-q', '--quiet', help='Silent mode, only log warnings', action='store_true')
    parser.add_argument('--dry-run', help='Noop, do not write anything', action='store_true')
    parser.add_argument('--date-from', help='Only import transaction >= date (YYYY-MM-DD)')
    parser.add_argument('-c', '--currency', metavar='ISOCODE',
                        help='Currency ISO code (default: EUR)', default='EUR')
    parser.add_argument('-f', '--gnucash-file', help='Gnucash data file')
    parser.add_argument('file', nargs='+', help='Input QIF file(s), can also be "mtp:<PATTERN>" '
                                                'to import from MTP device')

    main_args = parser.parse_args()
    import_qif.import_qif(main_args)

if __name__ == '__main__':
    main()
