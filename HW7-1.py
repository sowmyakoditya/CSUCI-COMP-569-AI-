# Sowmya Kodityala
# Devon Trammell
# Lean Xu
# Homework 7


from collections import defaultdict
from constraint import *



input = """530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
"""


print("\nInput state:\n\n" + input + "\n********************\n\nOutput State:\n\n")

# Populate the sudoku board
variables_with_number = {}
for i, line in enumerate(input.splitlines()):
    for j, val in enumerate(line):
        if val != '0':
            variables_with_number[f'm{i}{j}'] = int(val)

problem = Problem()
variables = []
groups = []
rows = defaultdict(list)
columns = defaultdict(list)
for q in range(3):
    for k in range(3):
        group = []
        for i in range(3):
            for j in range(3):
                var = f'm{(q*3)+i}{(k*3)+j}'
                variables.append(var)
                group.append(var)
                rows[f'{q*3 + i}'].append(var)
                columns[f'{k*3 + j}'].append(var)
        groups.append(group)

# Adding variables to the problem
variables_position = {v: i for i, v in enumerate(variables)}
for v in variables:
    number = variables_with_number.get(v)
    if number is None:
        problem.addVariable(v, range(1, 10))
    else:
        problem.addVariable(v, [number])

# Adding constraints to the problem 
for _, row in rows.items():
    problem.addConstraint(AllDifferentConstraint(), row)
for _, column in columns.items():
    problem.addConstraint(AllDifferentConstraint(), column)
for group in groups:
    problem.addConstraint(AllDifferentConstraint(), group)    

solution = problem.getSolution()

for i in range(9):
    line = []
    for j in range(9):
        line.append(solution[f'm{i}{j}'])
    print(line)

print("\n")