import sys
import numpy as np

'''
print("Enter the length N of the sequences.")
N = int(input())
if N > 200000:
    print("Enter N over 200,000.")
    sys.exit()
print("Enter the elements of the sequences a.")
a = []
for i in input().split():
    if int(i) >= 2**28:
        print("Enter elements below 268,435,456.")
        sys.exit()
    elif int(i) < 0:
        print("Enter elements over 0.")
        sys.exit()
    a.append(int(i))
print("Enter the elements of the sequences b.")
b = []
for j in input().split():
    if int(j) >= 2**28:
        print("Enter elements below 268,435,456.")
        sys.exit()
    elif int(j) < 0:
        print("Enter elements over 0.")
        sys.exit()
    b.append(int(j))
if (len(a) != N) or (len(b) != N):
    print("Enter N elements in the sequence a,b.")
    sys.exit()
S = [0] * 28
for i in range(N):
    for j in range(N):
        B = '{:028b}'.format(a[i] + b[j])
        for n in range(28):
            S[n] = S[n] + int(B[n])
XOR = ""
for n in range(28):
    if (S[n] % 2) == 0:
        XOR = XOR + "0"
    else:
        XOR = XOR + "1"
print(int(XOR, 2))
'''

# model answer
# enter the length N of the sequence a,b
print("Enter the length N of the sequences.")
N = int(input())
if N > 200000:
    print("Enter N over 200,000.")
    sys.exit()
# enter the sequence a
print("Enter the elements of the sequences a.")
aLt = input().split()
a = np.zeros(N, dtype=int)
for i, p in enumerate(aLt):
    if int(p) >= 2**28:
        print("Enter elements below 268,435,456.")
        sys.exit()
    elif int(p) < 0:
        print("Enter elements over 0.")
        sys.exit()
    a[i] = int(p)
# enter the sequence b
print("Enter the elements of the sequences b.")
bLt = input().split()
b = np.zeros(N, dtype=int)
for j, q in enumerate(bLt):
    if int(q) >= 2**28:
        print("Enter elements below 268,435,456.")
        sys.exit()
    elif int(q) < 0:
        print("Enter elements over 0.")
        sys.exit()
    b[j] = int(q)
# check the length of the sequence a,b
if (len(a) != N) or (len(b) != N):
    print("Enter N elements in the sequence a,b.")
    sys.exit()
# calculate XOR
b = np.sort(b)
XOR = ""
for n in range(28):
    amod = a % (2**(n+1))
    bmod = b % (2**(n+1))
    cycle = 2**n
    count = 0
    for k in range(N):
        T1 = cycle - amod[k]
        T2 = 2*cycle-amod[k]
        T3 = 3*cycle-amod[k]
        T4 = 4*cycle-amod[k]
        count = count + np.count_nonzero((bmod >= T1) & (bmod < T2)) \
                      + np.count_nonzero((bmod >= T3) & (bmod < T4))
    if count % 2 == 1:
        XOR = "1" + XOR
    else:
        XOR = "0" + XOR
print(int(XOR, 2))
