items = [["rice",2.4,8],["flour",1.9,5],["corn",4.7,6]]
# for item in items:
#     print(f"product: {item[0]} price {item[1]} Quality {item[2]} ")


# print(items[1][1])

# items[1][1]= items[1][1]*1.2
# print(items[1][1])

# items[1][1]= items[1][1]*1.2
# print(items[1][1])

# items[1][1]= 1
# print(items[1][1])

# items[1][1]= items[1][1]*.2
# print(items[1][1])


l = [2,4,8,16]

# print([i**3 for i in l])


def f1(x): return x*2
def f2(x): return x*4

lst =[]
for i in range(16):
    lst.append(f1(f2(i)))

# print(lst)

# ## ####################################list comprenhension
# print([f1(x) for x in range(64) if x in [f2(j) for j  in range(16)]])


##################################### list comprenhension another approch


# list1=[[1,2,3],[4,5,6]]

# print('output of this code !!!', [i*j for i in list1[0] for j in list1[1]])

############################ list comprenhension with string#################

words ='here is a stntence'.split()

print([[word ,len(word)] for word in words])

############################ sorted function with sting  
words = str.split('The longest word in this sentence')

print(sorted(words,key=len))

############################## case insensitive sorting########
sl = ['A','b','a','C','c']

sl.sort(key=str.lower)
print(sl)
sl.sort()
print(sl)


################ sort by index#########################

# items.sort(key=lambda item:item[1])

# print(items)

"""
    Function to iterate through a range of numbers and print each number.
    
    Parameters:
    low (int): The lower bound of the range.
    high (int): The upper bound of the range.
    
    Returns:
    None
"""
def iterTest(low,high):
    while low <= high:
        print('by iterator',low)
        low +=1


        
"""
    A function that recursively prints values from low to high.

    Parameters:
    low (int): The lower bound value.
    high (int): The upper bound value.
"""
def recursionTest(low,high):
    if low<=high:
        print('by recursion',low)
        recursionTest(low+1,high)

low =1
high = 10

val1 = iterTest(low,high)


val2 = recursionTest(low,high)


################### compare list with generator
import time

#create a generator function

def oddGen(n,m):
    while n < m:
        yield n
        n += 2

# buils a list of odd numbers between n and m

def oddLst(n,m):
    lst =[]
    while n < m:
        lst.append(n)
        n +=2
    return lst

# the time it takes to perform sum on an iterator

t1 = time.time()

sum(oddGen(1,1000000))
print("Time to sum an iterator: %f",(time.time()-t1))



# the time it takes to build and sum a list

t1 = time.time()
sum(oddLst(1,1000000))
print("Time to sum a list: %f",(time.time()-t1))
