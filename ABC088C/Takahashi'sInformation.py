import pandas as pd
import sys

# make dataframe to store the value of each coordinate
c = pd.DataFrame(index=[1, 2, 3], columns=[1, 2, 3])
# enter values for each coordinate
print("Enter the value c for each coordinate in row 1.")
c.iloc[0, 0], c.iloc[0, 1], c.iloc[0, 2] = (int(x) for x in input().split())
if sum(c.iloc[2, :] < 0) > 0 or sum(c.iloc[2, :] > 100) > 0:
    print("Enter an integer between 0 and 100.")
    sys.exit()
print("Enter the value c for each coordinate in row 2.")
c.iloc[1, 0], c.iloc[1, 1], c.iloc[1, 2] = (int(x) for x in input().split())
if sum(c.iloc[2, :] < 0) > 0 or sum(c.iloc[2, :] > 100) > 0:
    print("Enter an integer between 0 and 100.")
    sys.exit()
print("Enter the value c for each coordinate in row 3.")
c.iloc[2, 0], c.iloc[2, 1], c.iloc[2, 2] = (int(x) for x in input().split())
if sum(c.iloc[2, :] < 0) > 0 or sum(c.iloc[2, :] > 100) > 0:
    print("Enter an integer between 0 and 100.")
    sys.exit()

# find a,b that make up each coordinate values
if (c.iloc[0, 0] - c.iloc[1, 0]) != (c.iloc[0, 1] - c.iloc[1, 1]) or \
   (c.iloc[0, 1] - c.iloc[1, 1]) != (c.iloc[0, 2] - c.iloc[1, 2]) or \
   (c.iloc[0, 2] - c.iloc[1, 2]) != (c.iloc[0, 0] - c.iloc[1, 0]):
    print("No")
    sys.exit()
if (c.iloc[1, 0] - c.iloc[2, 0]) != (c.iloc[1, 1] - c.iloc[2, 1]) or \
   (c.iloc[1, 1] - c.iloc[2, 1]) != (c.iloc[1, 2] - c.iloc[2, 2]) or \
   (c.iloc[1, 2] - c.iloc[2, 2]) != (c.iloc[1, 0] - c.iloc[2, 0]):
    print("No")
    sys.exit()
if (c.iloc[2, 0] - c.iloc[0, 0]) != (c.iloc[2, 1] - c.iloc[0, 1]) or \
   (c.iloc[2, 1] - c.iloc[0, 1]) != (c.iloc[2, 2] - c.iloc[0, 2]) or \
   (c.iloc[2, 2] - c.iloc[0, 2]) != (c.iloc[2, 0] - c.iloc[0, 0]):
    print("No")
    sys.exit()
if (c.iloc[0, 0] - c.iloc[0, 1]) != (c.iloc[1, 0] - c.iloc[1, 1]) or \
   (c.iloc[1, 0] - c.iloc[1, 1]) != (c.iloc[2, 0] - c.iloc[2, 1]) or \
   (c.iloc[2, 0] - c.iloc[2, 1]) != (c.iloc[0, 0] - c.iloc[0, 1]):
    print("No")
    sys.exit()
if (c.iloc[0, 1] - c.iloc[0, 2]) != (c.iloc[1, 1] - c.iloc[1, 2]) or \
   (c.iloc[1, 1] - c.iloc[1, 2]) != (c.iloc[2, 1] - c.iloc[2, 2]) or \
   (c.iloc[2, 1] - c.iloc[2, 2]) != (c.iloc[0, 1] - c.iloc[0, 2]):
    print("No")
    sys.exit()
if (c.iloc[0, 2] - c.iloc[0, 0]) != (c.iloc[1, 2] - c.iloc[1, 0]) or \
   (c.iloc[1, 2] - c.iloc[1, 0]) != (c.iloc[2, 2] - c.iloc[2, 0]) or \
   (c.iloc[2, 2] - c.iloc[2, 0]) != (c.iloc[0, 2] - c.iloc[0, 0]):
    print("No")
    sys.exit()
print("Yes")

'''
# model answer
a1 = 0
b1 = c.iloc[0, 0] - a1
b2 = c.iloc[0, 1] - a1
b3 = c.iloc[0, 2] - a1
a2 = c.iloc[1, 0] - b1
a3 = c.iloc[2, 0] - b1
if (c.iloc[0, 0] != a1 + b1) or (c.iloc[0, 1] != a1 + b2) or \
   (c.iloc[0, 2] != a1 + b3) or (c.iloc[1, 0] != a2 + b1) or \
   (c.iloc[1, 1] != a2 + b2) or (c.iloc[1, 2] != a2 + b3) or \
   (c.iloc[2, 0] != a3 + b1) or (c.iloc[2, 1] != a3 + b2) or \
   (c.iloc[2, 2] != a3 + b3):
    print("No")
else:
    print("Yes")
'''
