import hashlib
import json
from merkletools import MerkleTools
from Transaction import Transaction


def calculate_hash(serial, previous_hash, timestamp, data):
    return hashlib.sha256(
        (str(serial) + str(previous_hash) + str(timestamp) + json.dumps(data)).encode('utf-8')).hexdigest()


class Block:

    def __init__(self, serial, transaction_list, merkelTreeRoot, timestamp, previous_hash, proof):
        self.serial = serial
        self.timestamp = timestamp
        self.transaction_list = transaction_list
        self.merkelTreeRoot = merkelTreeRoot
        self.previous_hash = previous_hash
        self.hash = calculate_hash(serial, timestamp, merkelTreeRoot, previous_hash)
        self.proof = proof

    def convertstring(self):
        return json.dumps({"serial": self.serial, "timestamp": self.timestamp, "merkelTreeRoot": self.merkelTreeRoot, "previous_hash": self.previous_hash, "hash": self.hash, "proof": self.proof, })


def buildtree(transactions: list[Transaction]):
    Merkle = MerkleTools(hash_type="md5")
    for i in transactions:
        Merkle.add_leaf(i.convertstring(), True)
        print(i)
    Merkle.make_tree()
    return Merkle.get_merkle_root()


'''
SANTHA MATE IMRE
HORA37
DEIK-PTI-MSC
2022-AUTUMN
'''
