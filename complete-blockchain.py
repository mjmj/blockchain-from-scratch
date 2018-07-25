#!/usr/bin/env python

from hashlib import sha256


class TXOutput(object):
'''output transactions'''

class TXInput(object):
'''input transactions'''

class Block(object):
'''blockchain block and related functionality'''

class BlockChain(object):
'''wrapper for blockchain and related functions'''

class ProofOfWork(object):
'''proof of work algorithm'''

class Transaction(object):
'''amalgamation of input and output transactions'''

class Utilities(object):
'''Helper methods'''

    def set_hash(self, hash_string):
        '''converts a string to a hash'''
        try:
            sha_sig = hashlib.sha256(hash_string.encode()).hexdigest()
            encoded_string = base58.b58encode(sha_sig)
        except Exception:
            raise
        return encoded_string.decode("utf-8")

