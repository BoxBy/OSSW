# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python

# making exception

class my_exception(Exception):
    def __init__(self):
        super().__init__("My exception happened")

try:
    raise my_exception
except Exception as e:
    print(e)

    