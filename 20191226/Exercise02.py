i = 91

print("i = ", i, " (dec)")
print("i = ", oct(i), " (oct)")
print("i = ", hex(i), " (hex)")
print("i = ", i, " (hex?)") # dec
# print("i = ", dec(i), " (dec)") 

for count in range(1001): # for(int i = 0; i < 1000; i++)
    print("{: 6}".format(count)) # {: >6} == setw(6)
print() # {:->6} == setw(6) << setfill('-')

print("{: >6}") # didn't helpful
for count in range(0, 1001, 10): # for(int i = 0; i < 1000; i *= 10)
    print(count)
print()

a = 5
b = 43
c = 104

print("{: >10}".format("Karen"), "{: <6}".format(a)) # > == right
print("{: >10}".format("Ben"), "{: <6}".format(b)) # < == left
print("{: >10}".format("Patricia"), "{: <6}".format(c))
print()

a1 = 1.05
b1 = 10.15
c1 = 200.87

print("{0:*>10.2f}".format(a1))
print("{0:*>10.2f}".format(b1))
print("{0:*>10.2f}".format(c1))