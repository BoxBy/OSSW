# https://github.com/BoxBy/Cpp/tree/master/20191121 : Cpp to Python

# queue & priority queue

import random
import queue

q = queue.Queue()

q.put(1) # python Queue using put as push
q.put(3)
q.put(5)
q.put(7)
q.put(11)

while q.qsize() :
    print(q.get()) # python Queue using get as pop


nums = queue.PriorityQueue()

howMany = int(input("How Many? : "))

for i in range(howMany) :
    next = random.randint(0, 100)
    print(next)
    nums.put(next)

del next
del howMany

print("\nPriority by Value : ")

while nums.qsize() :
    print(nums.get())