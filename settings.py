import os

AQBANKING_PATH = os.path.expanduser('~/.aqbanking/')
CACHE_PATH = os.path.join(AQBANKING_PATH, 'tmp')
BALANCE_PATH = os.path.join(CACHE_PATH, 'balance.ctx')