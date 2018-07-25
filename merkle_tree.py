#!/usr/bin/env python

import hashlib

ELEMENTS = [0, 1, 3] # Source elements of Merkle Tree
ROOT  = '' # Root hash of Merkle Tree

class MerkleTree(object):

    def __init__(self, hash_list):
        self.hash_list = hash_list
        self.elements = ELEMENTS

    def get_root(self):
        return ROOT

    def get_sha2_hex_value(self, hash_list):
        try:
            m = hashlib.sha256()
            m.update(hash_list)
        except Exception:
            raise
        return m.hexdigest()

    def get_next_merkle_row(self, merkle_row):
        '''
        Accepts the current row of the
        Merkle Tree and returns the next row
        '''
        # Determine if we need a leaf buddy to hash with
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

        # Hash leaf buddies together
        next_row = []
        for k in [hashed_row[x:x+2] for x in xrange(0, len(hashed_row), 2)]:
                # k is a list with two items that we'll hash together
                hasher = self.get_sha2_hex_value(k[0]+k[1])
                next_row.append(hasher)

        return next_row

    def merkle_tree(self):
        next_row = self.get_next_merkle_row(self.elements)

        # loop here to find root
        temptxlist = self.get_next_merkle_row(next_row)
        print temptxlist


if __name__ == "__main__":
    cls = MerkleTree(ELEMENTS)
    mk = cls.merkle_tree()
