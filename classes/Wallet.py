import uuid
import json
import os

class Wallet:

    def __init__(self,  unique_id = "", balance = 100, history = []):
        if unique_id == "" :
            # genere un nouveau wallet
            self.unique_id = self.generate_unique_id()
            self.balance = balance
            self.history = history
            self.save()
        else:
            # genere un wallet a partir d'un json
            self.unique_id = unique_id
            data = self.load()
            self.balance = data['balance']
            self.history = data['history']
        pass

    @staticmethod
    def generate_unique_id(self):
        unique_id = str(uuid.uuid4())
        # All files ending with .txt
        file_exists = os.path.exists('content/wallets/' + unique_id + '.json')
        if file_exists:
            unique_id = self.generate_unique_id()
        return unique_id
        
    def sub_balance(self, number):
        if (self.balance - number > 0):
            self.balance -= number
            return self.balance
        return False
    
    def add_balance(self, number):
        self.balance += number
        return self.balance
    
    def send(self, transaction, role, montant):
        if role == "emetteur":
            validation = self.sub_balance(montant)
            if validation == False:
                return False
        else:
            self.add_balance(montant)
        self.history.append(transaction)
        self.save()
    
    def save(self):
        data = {
            'unique_id': self.unique_id,
            'balance': self.balance,
            'history': self.history
        }

        pathToFile = 'content/wallets/' + self.unique_id + '.json'

        with open(pathToFile, 'w+') as outfile:
            str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)

    def load(self):

        pathToFile = 'content/wallets/' + self.unique_id + '.json'

        with open(pathToFile) as file:
            data = json.loads(file.read())
        return data


