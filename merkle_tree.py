#!/usr/bin/env python

import hashlib

ELEMENTS = [0, 1, 3] # Source elements of Merkle Tree
ROOT  = '' # Root hash of Merkle Tree

class MerkleTree(object):

    def __init__(self):
        pass

    def get_sha2_hex_value(self, string):
        try:
            m = hashlib.sha256()
            m.update(string)
        except Exception:
            raise
        return m.hexdigest()

    def get_next_merkle_row(self, merkle_row):
        '''
        Accepts the current row of the
        Merkle Tree and returns the next row
        '''

        # Determine if we need a buddy to hash with
        # Create a buddy if odd number of items
        list_len = len(merkle_row)
        while list_len % 2 != 0:
            merkle_row.extend(merkle_row[-1:])
            list_len = len(merkle_row)

        # Generate a list of hashes from elements
        hashed_row = []
        for index, item in enumerate(merkle_row, start=0):
            hashed = self.get_sha2_hex_value(str(item))
            hashed_row.append(hashed)

        # Hash buddies together
        next_row = []
        for key in [hashed_row[x:x+2] for x in xrange(0, len(hashed_row), 2)]:
                # k is a list with two items that we'll hash together
                hasher = self.get_sha2_hex_value(key[0]+key[1])
                next_row.append(hasher)

        return next_row


if __name__ == "__main__":
    cls = MerkleTree()
    mk = cls.get_next_merkle_row(ELEMENTS)
    print mk