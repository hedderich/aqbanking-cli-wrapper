import os

AQBANKING_PATH = os.path.expanduser('~/.aqbanking/')
PINFILE_PATH = os.path.join(AQBANKING_PATH, 'pinfile')
CACHE_PATH = os.path.join(AQBANKING_PATH, 'tmp')

BALANCE_PATH = os.path.join(CACHE_PATH, 'balance.ctx')
TRANSACTIONS_PATH = os.path.join(CACHE_PATH, 'transactions.ctx')