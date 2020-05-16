import math
AB, BC = int(input()), int(input())
degree_sign = u"\N{DEGREE SIGN}"
print(str(round(math.degrees(math.atan((AB/BC)))))+degree_sign)