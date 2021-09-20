

# Use iterators/generators on a custom collection to... 

class iterators:
    def __iteration__(self):
        self.next = 0
        return self
    def __init__(self, greater=0):
        self.greater = greater

    def __next_value__(self):
        if self.next <= self.greater:
            result = 2 ** self.next
            self.next += 1
            return result
        else:
            raise StopIteration

''''''''''
add ability to be used in a for in loop
add ability to be used in a list comprehension
add ability to convert to a list or other collection type
'''''''''

''''''''''
Create a decorator that adds behavior to a given function.
'''''''''
def generator(num):
    for j in range(num):
        yield num * num

def my_generators(num):
    return (x*x for x in range(num))

def print_my_generators(num):
    res = my_generators(num)
    for num in res:
        print(num)

def print_decorator(input):
    res = []
    for num in range(input):
        res.append(num * num)
    return res

# Anything else that catches your interest
def fun_one(char):
    results = [ ]
    for i in range(1,char+1):
        if char % i == 0: results.append(i)
    return results

def fun_two(char):
    for i in range(1,char+1):
        if char % i == 0: 
            yield i
print(fun_one(50))

for character in fun_two(50):
    print(character)