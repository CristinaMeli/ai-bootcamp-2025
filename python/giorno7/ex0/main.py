import csv
"""
Provo a sostituire direttamente in sorted con lambda
def f(person):
    return person[1],person[0]
"""
with open("data.csv") as fd:
    reader = csv.reader(fd)

    header = next(reader)

    sorted_csv = list(sorted(reader, key=lambda person: (person[1], person[0])))
    """ 
    # posso sostituire questo con la funzione enumerate
    count = 0
    for line in sorted_csv:
        count+=1
        print([count] + line)
    """
    for count, line in enumerate(sorted_csv, start=1):
        print([count] + line)

with open("data2.csv", 'w') as fd_out:
    writer = csv.writer(fd_out)
    writer.writerow(header)
    writer.writerows(sorted_csv)