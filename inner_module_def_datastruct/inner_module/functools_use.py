import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



# 函数装饰器
# functools.partial



# functools.partialmethod

# 序列的归并操作
# functools.reduce()

# functools.cmp_to_key()
# functools.singledispatch()
# functools.wraps()
# functools.total_ordering()

# functools.Any
# functools.Dict
# functools.Union
# functools.Callable
# functools.Generic
# functools.Optional
# functools.overload
# functools.Tuple
# functools.Type
# functools.TypeVar
# functools.WRAPPER_UPDATES
# functools.WRAPPER_ASSIGNMENTS

