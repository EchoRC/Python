#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import hashlib


class Block:

    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        sha256 = hashlib.sha256()
        sha256.update((str(self.index) + self.previousHash +
                       self.timestamp + self.data).encode('utf-8'))
        res = sha256.hexdigest()
        return res

    def __str__(self):
        return "index:" + str(self.index) + " timestamp:" + str(self.timestamp) + " data:" + str(self.data) + " previousHash:" + str(self.previousHash) + " hash:" + str(self.hash)


class Blockchain:

    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "01/01/2018", "Genesis block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def display(self):
        for i in range(len(self.chain)):
            print(self.chain[i])
            print("")


coin = Blockchain()
coin.addBlock(Block(1, "20/07/2018", "data-1", ""))
coin.display()
