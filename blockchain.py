#!/usr/bin/env python

import datetime
import json

from hashlib import sha256
from time import time


class StringUtil(object):

    def gen_hash(self, data):
        """Accepts a string and returns a
        sha256 hashed string
        """
        try:
            data = unicode(data, "utf-8")
            sha = sha256(data).hexdigest()
        except Exception:
            raise
        return sha

class Block(object):
    """Class definition for Block Object"""
    count = 0

    def __init__(self, data, previous_hash):
        self.util = StringUtil()
        self.previous_hash = previous_hash
        self.data = data
        self.ts = str(time())
        self.hash = self.calculate_hash()
        Block.count += 1
        self.block_id = Block.count

    def __repr__(self):
        return 'This Block\n\tID: {}, \n\thash: {}, \n\tprevious hash: '\
            '{}\n'.format(self.block_id, self.hash, self.previous_hash)

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data

    def get_timetstamp(self):
        return self.ts

    def calculate_hash(self):
        try:
            to_hash = self.previous_hash + self.ts + self.data
            result = self.util.gen_hash(to_hash)
        except:
            raise
        return result


class Blockchain(object):
    """Class definition for Main Chain"""
    def __init__(self, name='Main Chain'):
        self.name = name
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def view_chain(self):
        for block in self.chain:
            print block

    def validate_chain(self):
        """
        Simple validator. You'd want to use something like
        an in memory file to validate you blockchain in prod.
        """
        for x in range(len(self.chain) -1):
            if self.chain[x].calculate_hash() != self.chain[x+1].get_previous_hash():
                print 'There is a problem in the chain'

def block_generator(chain, blocks):
    """
    Method to generate & add blocks to your blockchain
    """
    block = Block('This Is Block 1', '0')
    chain.add(block)
    for x in range(blocks):
        next_block = Block('{}{}'.format('blockNum: ', x), block.get_hash())
        chain.add(next_block)
        block = next_block

if __name__ == "__main__":
    chain = Blockchain('Michael\'s Blockchain')
    block_generator(chain, 5)
    bad_block = Block('This is a bad block', '11010001101')
    chain.add(bad_block)
    chain.view_chain()
    chain.validate_chain()
