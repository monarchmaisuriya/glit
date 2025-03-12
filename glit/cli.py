import argparse
def main():
    """
    Main entry point for the script.
    """
    args = parse_args()
    args.func(args)

def parse_args():
    """
    Parse command line arguments using argparse.

    Returns:
        argparse.Namespace: arguments parsed from the command line
    """
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True
    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    return parser.parse_args()

def init(args):
    """
    Initialize function.
    """
    print('Hello, World!')