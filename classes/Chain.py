import hashlib

class Chain:

    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0
        pass

    def createHash(self):
        x = 0
        while True:
            x += 1
            hash = hashlib.sha256(str(x).encode()).hexdigest()
            if hash.startswith('0' * 4):
                return hash

    def verify_hash(self, baseHash):
        hash = hashlib.sha256(str(baseHash).encode()).hexdigest()
        if hash.startswith('0' * 4):
            return True
        return False
        