import re
import gzip
import io
import sys
import csv

filename = sys.argv[1]

pattern = r'(\w*\s+\d*\s\d{2}:\d{2}:\d{2})\s(\S*)\s(\S*):\s(\S*\s.{5})\s(\S*)\s-\s(\S*)\s(\S*)\s(\S*)\s"(\S*)"\s(\S*)\s(\S*)\s(\S*)\s"(\S*)"\s"(.*)"\s-\s(\S*):\s(\S*)\n$'

with open('log.csv', 'w') as fout:
    writer = csv.writer(fout, delimiter=';')
    with gzip.open(filename, 'rb') as f:
        with io.TextIOWrapper(f, encoding='utf-8') as decoder:
            for line in decoder:
                s = re.findall(pattern, line)
                if s == []:
                    continue
                result = s[0]
                writer.writerow(result)

