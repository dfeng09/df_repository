nums = [0,1,2,3,4,5,6,7,8,9,9]

#1. 循环
my_list = []
for i in nums:
    my_list.append(i)
print(my_list)
print('-------------------')

#2. 列表推导式
my_list = [i for i in nums]
print(my_list)
print('-------------------')

my_list = [i**2 for i in nums if i % 2 == 0]
print(my_list)
print('-------------------')

my_list = [i**2 if i % 2 == 0 else i**3 for i in nums]
print(my_list)
print('-------------------')

latters = 'abc'
numbers = '123'
my_list = [(i, j) for i in latters for j in numbers]
print(my_list)

#集合推导式
my_set = {i for i in nums}
print(my_set)



