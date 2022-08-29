import re
import gzip
import io
import sys

filename = sys.argv[1]

with open('log.csv', 'w') as fout:
    with gzip.open(filename, 'rb') as f:
        with io.TextIOWrapper(f, encoding='utf-8') as decoder:
            for line in decoder:
                s = re.split('\s', line)
                n = len(s)
                for i in range(n-1):
                    fout.write(s[i]+";")
                fout.write(s[n-1])
                fout.write("\n")




