# glit

Basic Git re-implementation in Python

## Installation

To install the package locally, run the following command:

```bash
$ pip install -e . --user
```

This will install your package in development mode, allowing you to run the `glit` command directly from your terminal

## Troubleshooting

If you’re still having issues after installing with pip:

1. Check if your PATH environment variable includes the directory where pip installs executables.
2. If you’re on Windows and using Git Bash, you might need to use `winpty` before your command if it’s hanging.
3. Verify that your cli.py file is correctly located in the glit package directory and is properly imported.

## Usage

To initialize a new glit repository:

```bash
$ glit init
```
