def decorator_function(function):
    def wrapper():
        print('*'*78)
        function()
        print('#'*78)
    return wrapper

@decorator_function
def name():
    print("Hello World!")
name()