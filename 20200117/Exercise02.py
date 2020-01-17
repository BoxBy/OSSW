# https://github.com/BoxBy/Cpp/tree/master/20191128 : Cpp to Python

import random

def printf(msg, a, len) :
    print(f"{msg}{a[:len]}")

length = 27
med = int(length / 2)

alpha = []
alph = list("abcdefghijklmnopqrstuvwxyz{")
for i in range(length - 1) :
    alpha.append(alph[i])

#print
print("Original")
# for i in range(length - 1) :
#     print(alpha[i], end = " ")
print(alpha)
# print()

#random shuffle
random.shuffle(alpha)
print("Random Shuffle")
# for i in range(length - 1) :
#     print(alpha[i], end = " ")
print(alpha)
# print()

alph[0:random.randint(0, len(alpha))].sort()
printf("\n\nAfter nth_element : ", alph, length)
printf("\n\t < median : ", alph, med)
printf("\n\t median : ", alph[med:], 1)
printf("\n\t > median : ", alph[med + 1:], med)
