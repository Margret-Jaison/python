#to print squareroot of anumbers between 1 and 500

from math import sqrt

for n in range(1, int(sqrt(500))+1):
    print(n * n)
