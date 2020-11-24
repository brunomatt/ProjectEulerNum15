#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
import math
#This is easily solvable with elementary number theory
#in a 2x2 grid, you must move down twice, DD, and right twice, RR.
#So we must arrange DDRR is as many unique ways as possible
#This is equivalent to the classic problem, "how many unique ways can you arrange the letters in MISSISSIPPI?"
#in our example DDRR can be arranged 4! / (2! * 2!) unique ways.

def unique_paths(m,n):
    answer = math.factorial(m+n) / (math.factorial(m) * math.factorial(n))
    print(int(answer))

unique_paths(20,20)