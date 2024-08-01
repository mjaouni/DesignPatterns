def type_check_decorator(types):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(f'Argument {a} is not of type {t}')
            # Check keyword arguments
            for key, value in kwargs.items():
                expected_type = types.get(key)
                if expected_type and not isinstance(value, expected_type):
                    raise ValueError(f'Keyword argument {key}={value} is not of type {expected_type} ')
            return fun(*args, **kwargs)

        return wrapper

    return decorator


# Usage

@type_check_decorator((int, int))
def add(a, b):
    return a + b


@type_check_decorator((str, int))
def repeat(text, times):
    return text * times


@type_check_decorator({'name': str, 'age': int})
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."


print(add(3, 4))  # Should Work
print(add('3', 4))  # Should Raise Error

print(repeat('hello-', 3))  # Should Work
print(repeat('hello-', 'aaaa'))  # Should Raise Error

print(introduce(name='Alex', age=35))  # Should Work
print(introduce(name='Alex', age='35'))  # Should raise Error
