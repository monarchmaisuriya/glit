import os
import hashlib

GIT_DIR = '.glit'

def init():
    """
    Create the directory for a new glit repository.
    """
    git_dir_path = os.path.join(os.getcwd(), GIT_DIR)
    
    if not os.path.exists(git_dir_path):
        os.mkdir(git_dir_path)
        os.makedirs(os.path.join(git_dir_path, 'objects'))
    else:
        raise Exception('A glit repository already exists in this directory')


def hash_object(data):
    """
    Compute the object id of some data and store it in .glit/objects.

    The object is stored verbatim in a file with the name of its object id.
    """
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):    
    """
    Retrieve the contents of an object from the glit repository.

    Args:
        oid(str): The object ID of the target object.

    Returns:
        bytes: The raw data read from the object file.
    """
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read()