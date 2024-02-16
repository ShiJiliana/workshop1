import math
r_blnd = float(input())
r_dist = float(input())
square = math.pi*(r_blnd**2 - r_dist**2)
print(abs(square))