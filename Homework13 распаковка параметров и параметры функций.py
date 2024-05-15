def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=1)
print_params(a=1, b='строка')
print_params(a=1, b='строка', c=True)

values_list = [17, 'список', True]
values_dict = {'a': 45, 'b': 'словарь', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2024, 'список 2']
print_params(*values_list_2, 42)

