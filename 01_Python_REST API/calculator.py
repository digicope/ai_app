# 함수 정의
def add(a,b):
    c = a + b
    print('add called!')
    return c

def subtract(a,b):
    c = a - b
    print('subtract called!')
    return c

def multiply(a,b):
    c = a * b
    print('multiply called!')
    return c

def divide(a,b):
    c = a / b
    print('divide called!')
    return c

print('calculator:',__name__)

if __name__ == '__main__':
    ret = add(10,20)
    print(ret)
