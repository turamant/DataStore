import csv

quoting = csv.QUOTE_ALL

with open('data/output_quoting.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting,
    )
    writer.writeheader()
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Petrov',
        'age': 30,
    })
    writer.writerow({
        'first_name': 'Dmitry',
        'last_name': 'Grishin',
        'age': 45,
    })
    writer.writerow({
        'first_name': 'Nikolay',
        'last_name': 'Baskov',
        'age': 43,
    })
