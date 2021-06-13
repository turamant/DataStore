import csv


with open('data/output.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
