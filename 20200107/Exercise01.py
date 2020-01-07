# https://github.com/BoxBy/Cpp/tree/master/20191017 : Cpp to Python

#include <iostream>

#using namespace std;

#class Task{
#    private:
#    static unsigned n;
#    public:
#    Task(){
#        n++;
#    }
#    ~Task(){
#        n--;
#    }
#    void CountN(){
#        cout << n << endl;
#    }
#};

#unsigned Task::n = 0;

#int main(){
#    Task a;
#    Task b;
#    Task c;
#    a.CountN();
#    b.CountN();
#    c.CountN();
#    return 0;
#}

# NOT python function

class Task:
    def __init__(self):
        self.__n = 0
    
    def Task(self):
        self.__n += 1

