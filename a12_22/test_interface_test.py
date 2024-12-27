
from interface_test import Rectangle

def test(x: int, y: int) -> None:
    r = Rectangle(x, y)
    a = r.area()
    b = r.perimeter()
    print(f'the length of {a}, is {b}')

if __name__ == '__main__':
    test(5, 10)

    
    