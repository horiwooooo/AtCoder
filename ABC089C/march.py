import sys

print("Enter the number N of person.")
N = int(input())
# make a list to store the names of people
names = []
# make a list to store the number of names starting with M,A,R,C,H
march = [0, 0, 0, 0, 0]
# enter names of people
for i in range(1, N+1, 1):
    print("Enter the name of the person " + str(i) + ".")
    name = input()
    if not name.isalpha():
        print("Enter an English name.")
        sys.exit()
    elif not name.isupper():
        print("Enter an uppercase name.")
        sys.exit()
    names.append(name)
    if name[0] == "M":
        march[0] = march[0] + 1
    elif name[0] == "A":
        march[1] = march[1] + 1
    elif name[0] == "R":
        march[2] = march[2] + 1
    elif name[0] == "C":
        march[3] = march[3] + 1
    elif name[0] == "H":
        march[4] = march[4] + 1
# calculate the number of selection that meet the conditions
pattern = 0
for p in range(len(march)-2):
    for q in range(p+1, len(march)-1, 1):
        for r in range(q+1, len(march), 1):
            pattern = pattern + (march[p]*march[q]*march[r])
print(str(pattern) + " patterns")
