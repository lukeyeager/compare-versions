import argparse
import sys

from . import core
from . import schemes

def main():
    """
    Module entry point

    Run with "python -m compare_versions"
    """
    parser = argparse.ArgumentParser(description='compare_versions')
    parser.add_argument('action', help='compare/verify')
    parser.add_argument('arguments', nargs='*', help='arguments to "action"')
    parser.add_argument('--stdin', action='store_true', help='Use stdin for input')
    args = parser.parse_args()

    if args.action is None:
        return interactive()

    if args.action == 'compare':
        if len(args.arguments) != 2:
            raise ValueError('This action requires two arguments')
        v1 = schemes.schemes['semver'](args.arguments[0])
        v2 = schemes.schemes['semver'](args.arguments[1])
        print('%s %s %s' % (v1, core.comparison_symbol(v1, v2), v2))

    elif args.action == 'verify':
        if len(args.arguments) < 1:
            raise ValueError('This action requires an argument: eq/ne/gt/lt/ge/le')
        comparison = args.arguments[0]
        if comparison not in ['eq','ne','gt','lt','ge','le']:
            raise ValueError('Invalid comparison "%s" - must be eq/ne/gt/lt/ge/le' % comparison)

        if len(args.arguments) < 3:
            raise ValueError('You must provide at least two versions to compare')
        versions = args.arguments[1:]

        return core.verify_list(versions, comparison)

    else:
        print('Unknown action: %s' % args.action)
        sys.exit(1)


if __name__ == '__main__':
    main()

