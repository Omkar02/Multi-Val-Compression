import re
import csv
from datetime import datetime

# yes this is working fine 
def get_chanded(pass_arr, flag):
    arr = []
    for GOT_IT in pass_arr:
        if GOT_IT != '?':
            if flag[0:7] == 'VARCHAR':
                ohh = "\'" + str(GOT_IT) + "\'"

            elif flag == 'INTEGER' or flag == 'BYTEINT':
                ohh = int(GOT_IT)

            elif flag == 'DATE':
                ohh = f'DATE(\'{GOT_IT}\')'

            elif flag == 'DECIMAL':
                ohh = float(GOT_IT)

            elif flag[0:9] == 'TIMESTAMP':
                ohh = f'TIMESTAMP(\'{GOT_IT}\')'

            else:
                ohh = GOT_IT

            arr.append(ohh)
    if len(arr) > 1:
        return '(' + (', '.join(map(str, arr)) + ')')
    else:
        return (', '.join(map(str, arr)))


def whitespace(func):
    return re.sub(r"^\s+|\s+$", "", func)
