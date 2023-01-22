import csv

with open('salaries.csv') as csvfile:
    info = list(csv.reader(csvfile))
    info.remove(info[0])

maxsal = 0
maxcandidate = []
for group in info:
    if int(group[0]) > int(maxsal):
        maxsal = group[0]

maxcandidate.append(
    f'Salary: {group[0]}, First Name: {group[1]}, Last Name: {group[2]}, Initials: {group[1][0]}{group[2][0]}'
    )

print(maxcandidate)
