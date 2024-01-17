list_num = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


def task_1():
    print('Задача 1')

    def fabric_func(sim, y):
        if sim == '*':
            def multiply(x):
                return x * y

            return multiply
        elif sim == '/':
            def division(x):
                return x / y

            return division
        else:
            raise Exception(f'Не могу распознать символ {sim}')

    divider = fabric_func(sim='/', y=2)
    multiplier = fabric_func(sim='*', y=2)
    result_divider = map(divider, (filter(int, list_num)))
    result_multiplier = map(multiplier, list_num)
    print(list(result_divider))
    print(list(result_multiplier))


def task_2():
    print('Задача 2')

    def squared(x):
        return x ** 2

    lambda_in_map = map(lambda x: x ** 2, list_num)
    print(list(lambda_in_map))
    lambda_func = lambda x: x ** 2
    func = map(lambda_func, list_num)
    print(list(func))
    lambda_with_def = map(squared, list_num)
    print(list(lambda_with_def))


def task_3():
    print('Задача 3')

    class Rect:
        def __init__(self, a, b):
            self.a, self.b = a, b

        def __call__(self, a, b):
            return a * b

    square = Rect(3, 4)
    print(square(2, 4))
    my_func = map(square, list_num, list_num)
    print(list(my_func))


try:
    task_1()
    task_2()
    task_3()
except Exception as exc:
    print(f'Что то не так :^) {exc}')
