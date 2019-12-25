def decorator_function(func):
    def wrapper(*args, **kwargs):
        print('Decorating 1')
        x=func(*args, **kwargs)
        print('Decorating 2')
        return x
    return wrapper


def external_function1(name):
    print(f'Hi 1 {name}')
    return name*2

def external_function2(name):
    print(f'Hi 2 {name}')
    return name*3
external_function2 = decorator_function(external_function2)

@decorator_function
def external_function3(name):
    print(f'Hi 3 {name}')
    return name*4


if __name__=='__main__':
    external_function1('Mika')

    external_function2('Mika')

    a = external_function3('Mika')
    print(a)
