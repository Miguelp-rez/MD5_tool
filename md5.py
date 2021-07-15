"""
This is a hashing tool designed to be run as a script. It uses the MD5 algorithm,
which generates a mesage digest of 128 bits or 16 bytes or 32 hex digits. This
program consumes bytes (by default) or UTF-8 strings (if specified).

Usage:
    python .\md5.py [--txt] .\path\to\filename
"""

import hashlib

"""
This function generates the md5 hash of some binary file.
"""
def hash_bytes(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        # Break down the file into chunks of 8192 bytes
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

"""
This function generates the md5 hash of some text file.
"""
def hash_text(filename):
    with open(filename, "r") as f:
        file_hash = hashlib.md5()
        # Break down the file into chunks of 8192 bytes
        while chunk := f.read(8192):
            # Change the encoding to UTF-8
            chunk= chunk.encode('utf-8')
            file_hash.update(chunk)
    return file_hash.hexdigest()

# The following is only run when the script is not imported.
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='MD5 hashing tool. By default the input file is encoded as bytes.'
        )
    parser.add_argument('filename', type=str, help='Relative or absolute path to the file.')
    parser.add_argument('--txt', action='store_true', help='text file.')   
    args = parser.parse_args()
    if args.txt:
        msg_digest = hash_text(args.filename)
    else:
        msg_digest = hash_bytes(args.filename)
    print(msg_digest)