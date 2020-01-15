# https://github.com/BoxBy/Cpp/tree/master/20191121 : Cpp to Python

# stack

prompt = "Enter an algebraic expression : "
lparen = '('
rparen = ')'

stack = [] # using as stack

buf = input(prompt)

for i in buf :
    stack.extend(i)

print("OG expression : {}".format(buf))

print("Expression in reserve : ", end = '')

while stack :
    t = stack.pop()

    if t == lparen :
        t = rparen
    elif t == rparen :
        t = lparen
    print(t, end = '')

print()

