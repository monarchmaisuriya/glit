import argparse
import os 
import sys
from . import base
from . import data
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
    
    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')
    
    get_object_parser = commands.add_parser('get-object')
    get_object_parser.set_defaults(func=get_object)
    get_object_parser.add_argument('object')
    
    write_tree_parser = commands.add_parser('write-tree')
    write_tree_parser.set_defaults(func=write_tree)
    
    return parser.parse_args()

def init(args):
    """
    Initialize empty glit repository.
    """
    data.init()
    print (f'Initialized empty glit repository in {os.getcwd()}/{data.GIT_DIR}')
    

def hash_object(args):
    """
    Read a file and compute its SHA-1 object hash.

    Given a file as input, print its SHA-1 object hash to stdout.
    """
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))
        

def get_object(args):    
    """
    Retrieve the contents of an object from the glit repository.

    Given a glit object id as input, print the contents of the object to stdout.
    """
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))

def write_tree (args):
    print(base.write_tree())