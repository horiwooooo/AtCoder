print("Enter a string composed of lowercase letters.")
S = input()
pos = 0

while pos < len(S):
    if S[pos:pos+5] == "dream":
        if S[pos+5:pos+7] == "er":
            if S[pos+5:pos+10] == "erase":
                # determine "dream"
                pos = pos + 5
            else:
                # determine "dreamer"
                pos = pos + 7
        else:
            # determine "dream"
            pos = pos + 5
    elif S[pos:pos+5] == "erase":
        if S[pos+5:pos+6] == "r":
            # determine "eraser"
            pos = pos + 6
        else:
            # determine "erase"
            pos = pos + 5
    else:
        print("NO")
        break
else:
    print("YES")

'''
# Model Answer
s = input()
s = s.replace('eraser', '')
s = s.replace('erase', '')
s = s.replace('dreamer', '')
s = s.replace('dream', '')
if s:
  print('NO')
else:
  print('YES')
'''
