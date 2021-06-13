import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = '*'
    delimiter = '!'
    lineterminator = '\n'

csv.register_dialect('tester', CustomDialect)

with open('data/output_5_class.csv', 'w') as f:
    writer = csv.writer(f, dialect='tester')
    for i in range(5):
        writer.writerow(['1', '2', '3'])