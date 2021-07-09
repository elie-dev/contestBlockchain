import uuid
import json
import os
import hashlib
from classes.Wallet import *

class Block:
    def __init__(self, hash = "", parent_hash = "", base_hash = 1 ):
        if hash == "" :
            # genere un nouveau wallet
            self.parent_hash = parent_hash
            self.base_hash = base_hash
            self.hash = self.createHash(base_hash)
            self.transactions = {}
            self.save()
        else:
            # genere un wallet a partir d'un json
            self.hash = hash
            data = self.load(hash)
            self.parent_hash = data['parent_hash']
            self.base_hash = data['base_hash']
            self.transactions = data['transactions']

    def createHash(self, baseHash):
        h = hashlib.sha256(str(baseHash).encode())
        return h.hexdigest()

    def check_hash(self):
        newHash = self.createHash(self.base_hash)
        if newHash != self.hash:
            return False
        return True

    def get_weight(self):
        path = 'content/blocs/' + self.hash + '.json'
        return os.stat(path).st_size

    def add_transaction(self, emetteurName, recepteurName, montant):
        emetteur = Wallet(emetteurName)
        recepteur = Wallet(recepteurName)
        t = str(uuid.uuid1())
        a = {
            t: {
                "walletEmetteur": emetteurName,
                "walletRecepteur": recepteurName,
                "montant": montant
            }
        }
        validation = emetteur.send(a, "emetteur", montant)
        if validation == False:
            print("transaction annulé solde insufisant")
            return
        recepteur.send(a, "recepteur", montant)
        self.transactions.update(a)
        self.save()

    def get_transaction(self, transaction):
        return self.transactions[transaction]

    def save(self):
        data = {
            'hash': self.hash,
            'base_hash': self.base_hash,
            'parent_hash': self.parent_hash,
            'transactions': self.transactions
        }

        pathToFile = 'content/blocs/' + self.hash + '.json'

        with open(pathToFile, 'w+') as outfile:
            str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)

    def load(self, hash):
        pathToFile = 'content/blocs/' + hash + '.json'

        with open(pathToFile) as file:
            data = json.loads(file.read())
        return data