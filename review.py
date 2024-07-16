# review.py
# Author: Joey Xie
# Data: July 16th 2024

# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

# Answer:
# Describe:  This function is used to add value into a list, and it has two arguments; The second argument is a list which has a default value of [];
# Knowledge: List is a mutable object(which can be passed out of the function), and [] will new a list object which is mutable;
# Error:     There might be some unexpected behavior when this function is used without the second argument; since list is a mutable object, when the first time this function is used without second argument, a list object is created and stored; 
#            If the function is called without the second argument again, the list created when first called will be passed in and it is containing unexpected values already;
# Solution:  Change the default value of second argument to None which will not change how this function is called, and as long as it is None, a new list will be created, the value will be stored in this new list; 

def add_to_list_revised(value, my_list=None):
    if (my_list is None):
        my_list = []
    my_list.append(value)

    return my_list

# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."

# Answer:
# Describe:  This function is used to format a greeting line with two arguments, and these two inputs are supposed to be filled into the greeting line;
# Error:     These two arguments are not useful for this fucntion, changing these two arguments will not affect the output of this function, and this behavior is not expected;
# Solution:  Add a format f befor the first ", also in order to ensure the arguments are useful and format a proper greeting line, it might be useful to check the inputs type; (More defensive, not forced)

def format_greeting_revised(name:str, age:int):

    return f"Hello, my name is {name} and I am {age} years old."

# Review 3

class Counter:

    count = 0

    def __init__(self):

        self.count += 1

 

    def get_count(self):

        return self.count

# Answer:
# Describe:   This is class being used as a counter to keep track on counts, it has a public attribute count and a constructor function which will add 1 into count, and a get_count function to get the count value to keep track;
# Knowledge:  A public attribute is accessible outside the class, therefore, the count attribute can be get and set easily; Also in convention, a get function normally would be followed by a set function, and as a counter, it should have a reset function;
# Error:      As being describe, this class has an important attribute count, which cane be accessed imporperly by unexpected behavior, so the class's encapsulation is poor; 
# Solution:   Therefore, this attribute should be changed into private;
#             Also as suggestion, this counter class should also have (not forced)     reset function: reset the count back to 1 as designed,              add_count fucntion: add value into count to keep track; 

class RevisedCounter:
    __count = 0

    def __init__(self):
        self.__count = 1

    def get_count(self):
        return self.__count
    
    def reset_count(self):
        self.__count = 1
    
    def add_count(self, value):
        self.__count += value

# Review 4

import threading

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Answer:
# Describe: The program above describes a muti-threading system to add count on the counter, it has 10 threads to run the worker cuntion, and each worker function thread would run 1000 times of counter.increment() function, 
#           the expect count on the counter should be 10000;
# Error:    When a program involve muti-threading, we need to ensure it is thread-safe, in worker function, it will run the object counter's increment function; it is clear that this function is not thread-safe, during multi-threading it is 
#           called by many threads at the same time, the counter.count might be unexpected at that time and the count value might not be able to reach 10000 as expected;
# Solution: Add a thread lock on the increment function;

class RevisedSafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.lock.acquire()
        try:
            self.count += 1
        finally:
            self.lock.release()


def worker(counter):
    for _ in range(1000):
        counter.increment()

counter2 = SafeCounter()

threads2 = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter2,))
    t.start()
    threads2.append(t)

for t in threads2:
    t.join()

# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts

# Answer:
# Describe: The function above is to coudn the occurrence of the input list;
# Error:    The element in the input list has no type check, as the key of directory, the element must be hashable. Also the operation =+ is not functioning should be changed to +=
# Solution: Add a hashable check and change the operation to +=, if the element is not hashable, do not count its occurance;

def is_hashable(data):
    try:
        hash(data)
        return True
    except TypeError:
        return False

def count_occurrences1(lst):
    counts = {}
    for item in lst:
        if not is_hashable(item):
            continue
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


