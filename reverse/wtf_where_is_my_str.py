import sys

verify = [521, 339, 1028, 365, 1132, 352, 833]
if len(sys.argv[1]) != len(verify):
    sys.exit(-1)

for i in range(7):
    char = ord(sys.argv[1][i])
    char = (char + i) * 13 -337
    if char != verify[i]:
        sys.exit(-1)