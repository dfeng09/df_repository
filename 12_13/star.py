#打包，解包
nums = [1,2,3,4,5]
first, *second = nums
print(first)
print("********")
print(second)

def test(*args):
    print(args)
test(1,2,3,4,5)

def example(**kwargs):
    print(kwargs)
example(name='keqing', age=18)