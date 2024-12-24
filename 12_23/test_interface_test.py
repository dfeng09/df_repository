from interface_test import *

def test(x: int, y: int) -> None:
    r = Rectangle(x,y)
    a = r.area()
    b = r.perimeter()

if __name__ == '__main__':
    test()
    
    