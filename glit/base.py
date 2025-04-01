import os
from . import data

def write_tree (directory='.'):
    """
    Write the contents of the given directory to the glit database, and return its
    tree object ID.

    :param directory: The directory to write. Defaults to the current directory.
    :return: The object ID of the tree object.
    """
    entries = []
    with os.scandir (directory) as it:
        for entry in it:
            full = f'{directory}/{entry.name}'
            if is_ignored (full):
                continue

            if entry.is_file (follow_symlinks=False):
                type_ = 'blob'
                with open (full, 'rb') as f:
                    oid = data.hash_object (f.read ())
            elif entry.is_dir (follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree (full)
            entries.append ((entry.name, oid, type_))

    tree = ''.join (f'{type_} {oid} {name}\n'
                    for name, oid, type_
                    in sorted (entries))
    return data.hash_object (tree.encode (), 'tree')


def is_ignored (path):
    """
    Return whether the given path should be ignored.

    :param path: The path to test.
    :return: ``True`` if the path should be ignored, ``False`` otherwise.
    """
    return '.glit' in path.split ('/')