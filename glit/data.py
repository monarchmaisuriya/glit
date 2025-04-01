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


def hash_object (data, type_='blob'):
    """
    Compute the hash of an object and store it in the glit repository.

    Store the given data under the given type (default 'blob') in the glit
    repository.  The SHA-1 object hash of the resulting object is returned.
    """
    obj = type_.encode () + b'\x00' + data
    oid = hashlib.sha1 (obj).hexdigest ()
    with open (f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write (obj)
    return oid


def get_object (oid, expected='blob'):
    """
    Retrieve the contents of an object from the glit repository.

    Args:
        oid (str): The object ID of the glit object to retrieve.
        expected (str, optional): The expected type of the object, defaults to 'blob'.

    Returns:
        bytes: The content of the object.

    Raises:
        AssertionError: If the object's actual type does not match the expected type.
    """

    with open (f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read ()

    type_, _, content = obj.partition (b'\x00')
    type_ = type_.decode ()

    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content