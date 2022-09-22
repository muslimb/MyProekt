a = input('Файл в фаста формате 1: ')
b = input('файл в фаста формате 2: ')
from Bio.SeqIO import parse
file = open(a)
records = parse(file, 'fasta')
for record in records:
    record.seq

file1 = open(b)
humans = parse(file1, 'fasta')
for human in humans:
    human.seq

a = record.seq
b = human.seq
c = len(human.seq)
for i in range(c):
    if b[i:i+5] in a:
        print(b[i:i+5])

print('Результаты готов!')