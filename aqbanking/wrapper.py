import csv
from datetime import datetime
from decimal import Decimal
import os
from subprocess import check_output, run
import sys

from aqbanking import settings
from aqbanking.utils import cache_dir_required


def list_accounts():
    stdout = check_output(['aqhbci-tool4', 'listaccounts'])

    account_list = []
    for account_row in stdout.decode(sys.stdout.encoding).split('\n'):
        account_row = account_row.split()
        if len(account_row):
            account_list.append({'account_name': account_row[1][:-1],
                                 'bank_code': account_row[3],
                                 'account_number': account_row[6]})
    return account_list


@cache_dir_required
def request_balance():
    run(['aqbanking-cli', '-n',
         '-P', settings.PINFILE_PATH,
         'request', '--balance',
         '-c', settings.BALANCE_PATH])
    stdout = check_output(['aqbanking-cli', 'listbal',
                           '-c', settings.BALANCE_PATH])

    os.remove(settings.BALANCE_PATH)
    response = stdout.decode(sys.stdout.encoding).split('\t')

    if len(response) > 13:
        return {'bank_code': response[1],
                'account_number': response[2],
                'timestamp': datetime.strptime(' '.join(response[5:7]),
                                               '%d.%m.%Y %H:%M'),
                'amount': Decimal(response[7]),
                'currency': response[8]}


@cache_dir_required
def request_transactions():
    run(['aqbanking-cli', '-n',
         '-P', settings.PINFILE_PATH,
         'request', '--transactions',
         '-c', settings.TRANSACTIONS_PATH])
    stdout = check_output(['aqbanking-cli', 'listtrans',
                           '-c', settings.TRANSACTIONS_PATH])

    os.remove(settings.TRANSACTIONS_PATH)
    response = csv.DictReader(stdout.decode(sys.stdout.encoding).splitlines(),
                              delimiter=';')

    transactions = []
    for row in response:
        transactions.append({'date': datetime.strptime(row['date'], '%Y/%m/%d'),
                             'valuta_date': datetime.strptime(row['valutadate'],
                                                              '%Y/%m/%d'),
                             'value_value': Decimal(row['value_value']),
                             'value_currency': row['value_currency'],
                             'remote_name': ' '.join([row['remoteName'],
                                                      row['remoteName1']]),
                             'remote_account_no': row['remoteAccountNumber'],
                             'remote_bank_code': row['remoteBankCode'],
                             'purpose': ''.join([row['purpose'],
                                                 row['purpose1'],
                                                 row['purpose2'],
                                                 row['purpose3'],
                                                 row['purpose4'],])})
    return transactions