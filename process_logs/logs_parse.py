import re
import gzip
import io
import sys
import csv

filename = sys.argv[1]

with open('log.csv', 'w') as fout:
    writer = csv.writer(fout, delimiter=';')
    with gzip.open(filename, 'rb') as f:
        with io.TextIOWrapper(f, encoding='utf-8') as decoder:
            for line in decoder:
                s = re.split('\s', line)
                writer.writerow(s)
                
