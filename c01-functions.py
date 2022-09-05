# Class 01 - Intro
# Author: João Chrisóstomo Ribeiro Abegão

# Function definition
# function with print
def bhaskara(a, b, c):
    x1 = (b*(-1) + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (b*(-1) - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    print(x1, x2)

# function with return
def bhaskara2(a, b, c):
    x1 = (b*(-1) + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (b*(-1) - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    return x1, x2


# Main code
if __name__ == '__main__':

    bhaskara(1, 12, -13)   # x1 = 1.0 and x2 = -13.0
    bhaskara(2, -16, -18)  # x1 = 9.0 and x2 = -1.0
    print(16*'-----')
    print(bhaskara2(2, -16, -18))
    xa, xb = bhaskara2(2, -16, -18)
    print(xa, xb)