from os import waitpid
from classes.Wallet import *
from classes.Block import *
from classes.Chain import *
bloc = Block("6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b")
#transaction = bloc.add_transaction("0a2e5bac-4d0d-4260-b9e6-324eee5e2564", "20a812c3-1610-4bec-831f-1bba023fcd49", 100)
#transaction = bloc.get_transaction("77727228-dff2-11eb-8563-04d4c47c6a59")

chain = Chain()
transaction = chain.createHash('a')
print(transaction)