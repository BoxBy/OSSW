# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python
# Python didn't have pointer, const


def unsigned(n):
  return n & 0xFFFFFFFF
  

int_val = 123
float_val = float(int_val) # casting

f = -6.9072
a = 100

print(float_val)

t = unsigned(f) # unsigned
print(t)