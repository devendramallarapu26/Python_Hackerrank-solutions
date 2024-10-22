x = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    x.append([score, name])
x.sort()
minimum_score = x[0][0]
while x != [] and x[0][0] == minimum_score:
    x.pop(0)
if x != []:
    second_minimum_score = x[0][0]
    for b in x:
        if b[0] == second_minimum_score:
            print(b[1])
# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.          
          
