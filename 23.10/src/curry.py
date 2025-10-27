def curry(f: callable, arg_count: int) -> callable:
    if arg_count < 0 or arg_count != f.__code__.co_argcount:
        raise ValueError("Некорректное значение арности")

    def curried(*collected_args):
        if len(collected_args) < arg_count:

            def next_arg(new_arg):
                return curried(*(list(collected_args) + [new_arg]))

            return next_arg
        elif len(collected_args) == arg_count:
            return f(*collected_args)
        else:
            raise ValueError(
                "Общее количество аргументов больше нужного \
(например, если передано слишком много аргументов в каком-то из вызовов)"
            )

    return curried


def uncurry(f: callable) -> callable:
    if not callable(f):
        raise ValueError("Передана не функция")

    def uncurried(*args):
        res = f
        if len(args) == 0:
            try:
                res = res()
            except TypeError:
                raise TypeError from TypeError

        for i in args:
            if not callable(res):
                raise ValueError("Передано слишком много аргументов")
            res = res(i)

        if callable(res):
            raise ValueError("Передано недостаточно аргументов")

        return res

    return uncurried
