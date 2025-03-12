import os

GIT_DIR = '.glit'

def init ():
    """
    Create the directory for a new glit repository.
    """

    os.makedirs (GIT_DIR)