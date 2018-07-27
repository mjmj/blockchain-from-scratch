#!/usr/bin/env python

import json
import datetime
from time import time
from hashlib import sha256

DIFFICULTY = 2
NONCE = 100


class Utilities(object):
    """Helper methods"""

    def set_hash(self, hash_string):
        """Converts a string to a hash"""
        try:
            data = unicode(data, "utf-8")
            sha = sha256(data).hexdigest()
        except Exception:
            raise
        return sha

    def hash_2_hex_string(self, byte_array):
        """Converts hash to displayable string"""
        return byte_array.decode("utf-8")


class TXOutput(object):
    """Output transactions"""

    def __init__(self, sender, value, block_txid):
        self.block_txid = block_txid
        self.value = value
        self.sender = sender

    def get_value(self):
        return self.value

    def get_sender(self):
        return self.sender

    def get_tx_id(self):
        return self.txid

    def can_unlock_output_with(self, data):
        """Accepts a string of expected identity & confirms the
        identity of a sender. Returns true if user identifier
        matches the sender of this transaction."""
        if self.person == data:
            return True

    def __repr__(self):
        return 'This Block\n\tTXID: {}, \n\t value: {}, \n\tsender: '\
            '{}\n'.format(self.block_txid, self.value, self.sender)

class TXInput(object):
    """Input transactions"""

    def __init__(self, receiver, block_txid, msg):
        self.block_txid = block_txid
        self.receiver = receiver # prob need to be more explicit here

    def get_receiver(self):
        return self.receiver

    def get_tx_id(self):
        return self.txid

    def can_unlock_output_with(self, data):
        """Accepts a string of expected identity & confirms the
        identity of a person. Returns true if user identifier
        matches the person of this transaction."""
        if self.receiver == data:
            return True

    def __repr__(self):
        return 'This Block\n\tTXID: {}, \n\t value: {}, \n\treceiver: '\
            '{}\n'.format(self.block_txid, self.value, self.receiver)


class Transaction(object):
    """wrapper for the inputs and outputs of a transaction
    (debits & credits)"""

    def __init__(self, inputs, outputs, txid):
        self.inputs = inputs
        self.outputs = outputs
        self.txid = txid

    def set_id(self):
        """Initializes the transaction id to a count of transactions.
        Increments the count."""
        self.txid += 1

    def new_coinbase_tx(self, person, dest, msg):
        """Creates a coinbase transaction"""
        txInput = TXInput("", -1, msg)
        txOutput = TXOutput("", 100, msg)
        coinbase_tx = Transaction(txInput, txOutput, -1)
        return txInput

class ProofOfWork(object):
    """Proof of work algorithm"""

    def __init__(self, difficulty, current_block):
        self.difficulty = difficulty               # Mining Difficulty
        self.mask = [0] * difficulty               # Mask from Mining
        self.nonce = 0
        self.max_nonce = 133700000
        self.current_block = current_block         # Target Block

    def prepare_data(self):
        blk_header = Block().get_data() + (NONCE+1)
        return blk_header

    def run(self):
        """Mine the block stored in the class"""
        prepare_data() # do something here

class Block(object):
    """Blockchain block and related functionality"""
    count = 0

    def __init__(self, txs, previous_hash):
        self.ts = datetime.datetime.now()
        self.previous_hash = previous_hash
        Block.count += 1
        self.block_height = Block.count
        self.txs = txs
        self.hash = self.get_data(). # this isn't going to work
        self.block_id = Block.count
        self.current_hash = Utilities().set_hash(self.hash)
        proof_of_work = ProofOfWork(DIFFICULTY, current_block)
        proof_of_work.mine() # impliment this

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_txs(self):
        return self.txs

    def get_block_id(self):
        return self.block_id

    @staticmethod
    def new_block(txs, previous_hash):
        block = Block(txs, previous_hash)
        return block

    def hash_txs(self):
        hash_block = new_block(self.txs) # this is f'd

    def display_txs(self):
        for tx in self.txs:
            if type(tx) == InputTx:
                print tx
        for tx in self.txs:
            if type(tx) == OutputTx:
                print tx

    def get_data(self):
        try:
            to_hash = self.previous_hash + self.hash + self.ts
            result = Utilities().set_hash(to_hash)  # initialize Utilities once above
        except:
            raise
        return result


class BlockChain(object):
    """Wrapper for blockchain and related functions"""

    def __init__(self, chain=[], blocklist=[], name='Main Chain'):
        self.name = name
        self.chain = []
        self.blocklist = []
        self.genesis_block = self.create_genesis_block(blocklist)

    def add_block(self, txs):
        """Creates a new block using transactions
        passed to it"""
        new_block = Block.new_block(txs)
        self.save_to_file(new_block)

    def save_to_file(self, data):
        """Writes out blockchain to a json file"""
        try:
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
        except:
            raise

    def create_genesis_block(self, txs):
        """ Accepts an array of transactions
        and creates the first block"""
        self.chain.append(Block.new_block(txs, ''))

    def start_blockchain(self):
        """ Creates a coinbase tx, adds it to a block
        adds block to blockchain"""
        coinbase = Transaction().new_coinbase_tx('', dest, 'coinbase_tx') # what is destination?
        new_blk = create_genesis_block(coinbase)
        add_blk = self.add_block(new_blk)

    def contains_input_tx(self, tx_output):
        """Finds unused transactions"""
        # Search for the output transaction in the list of input transactions
        for block in self.chain:
            print block
        for tx in tx_output:
            if tx_output == tx_input:
                return True
            else:
                return False

    def find_utxo(self, person):
        """Finds unspent transactions for a person"""
        tx_output = []
        for block in self.chain:
            for tx in self.blocklist:
                print 'poop'
        return utxo

    def new_output_tx(self, sender, receiver, amount):
        """Send money from one person to another"""
        utxo = self.find_utxo(sender)
        tx_inputs = []
        tx_outputs = [utxo]
        # more stuffs here

    def get_balance(self, person):
        """Returns balance for a person"""
        total = []
        for utxo in self.contains_input_tx():
            total.append(utxo)
        return total
