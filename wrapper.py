from subprocess import check_output
import sys


def list_accounts():
    stdout = check_output(['aqhbci-tool4', 'listaccounts'])

    account_list = []
    for account_row in stdout.decode(sys.stdout.encoding).split('\n'):
        account_row = account_row.split()
        if len(account_row):
            account_list.append({'account_name': account_row[1][:-1],
                                 'bank': account_row[3],
                                 'account_number': account_row[6]})
    return account_list