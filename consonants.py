
# purposely have 8 consonants, half upper, half lower. on run answer comes back 4, its counting only lowerself.
# need to understand how to .upper .lower

c = "TH th dg DG"

numC = 0

for char in c:
    if char == 'b' or char == 'c' or char == 'd' or char == 'f' or char == 'g' or char == 'h' \
        or char == 'j' or char == 'k' or char == 'l' or char == 'm' or char == 'n' or char == 'p' \
        or char == 'q' or char == 'r' or char == 's' or char == 't' or char == 'v' or char == 'w' \
        or char == 'x' or char == 'w' or char == 'z':
            numC += 1

print('Number of consonants is: ' + str(numC))
