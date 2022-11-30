
# ---------------> EXAMPLE 01<-------------
def greed():
    print('hello every one')
greed()

# using lambda funcion
greed_ = lambda : print("hi every one")
greed_()



# ---------------> EXAMPLE 02<-------------
def max_(a,b):
    if a>b:
        return a
    else:
        return b
print(max_(6,8))

# using lambda funcion
_max = lambda a,b: a if a>b else b
print(_max(3,5))


# ---------------> EXAMPLE 03<-------------
s = 'Phitron'
new_str = lambda S : S.upper()[::-1] # start : end : step, here start and end is empty
print(new_str(s))


# ---------------> EXAMPLE 04<-------------
lst = [2,3,4,5,6,7]
def double(x):
    return x*2
for item in lst:
    print(double(item))

# using lambda function
new_lst = [lambda arg = x : arg*2 for x in lst]
for item in new_lst:
    print(item())

# ---------------> EXAMPLE 05 filter<-------------
even_list = list(filter(lambda x : (x%2 == 0),lst)) # filter return value based on specific condition.
print(even_list)

