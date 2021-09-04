''' to print 1234
             234
             34
             4

'''
s='1234'
for i in range(4):
    print(s[i:])

''' to print APQR
             ABQR
             ABCR
             ABCD '''

s1='ABCD'
s2='PQR'
for i in range (4):
    print(s1[:i+1]+s2[i:])

