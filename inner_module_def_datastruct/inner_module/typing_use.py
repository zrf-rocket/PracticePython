from inner_module_def_datastruct import WEIXIN_URL, AUTHOR, AGE
from typing import List, Tuple, Dict, Set

# 可以使用typing中的基本类型来声明变量的类型，如int，float，bool，str等
name: str = AUTHOR
age: int = 25
height: float = 1.75
active: bool = True
blog: str = WEIXIN_URL

numbers_list: List[int] = [1, 2, 3, 4, 5]
numbers_tuple: Tuple[int, float, str] = (1, 1.0, "1")
numbers_dict: Dict[str, int] = {"one": 1, "two": 2, "three": 3}
numbers_set: Set[str] = {"one", "two", "three"}

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers(numbers_list))



from typing import Union, Any, Optional

# Union 表示联合类型，可以用来表示多种不同类型的变量（定义一个变量可以是多个类型中的任何一个）；而 Any 则表示任意类型，可以用来表示一个变量可以是任何类型。
result: Union[str, int, float] = 1
value: Optional[int] = None
anything: Any = 42

if result == 1:
    # result is now a string, not an int.
    result = WEIXIN_URL
print(result)



from typing import TypeVar, Generic

T = TypeVar('T')

class Singleton(Generic[T]):

    _instance: T = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(Singleton):
    pass

class Bar(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()
bar = Bar()

print(foo1 is foo2)  # True
print(foo1 is bar)  # False


def my_func(num: int, my_str: str) -> bool:
    if num > 10 and my_str == WEIXIN_URL:
        return True
    else:
        return False

print(my_func(AGE, WEIXIN_URL))
print(my_func(1.2, False))



def my_optional_func(num: Optional[int]) -> bool:
    if num is not None and num > 10:
        return True
    else:
        return False

# my_optional_func()  # 虽然参数可以为None，但依然需要传递None，否则报错：TypeError: my_optional_func() missing 1 required positional argument: 'num'
my_optional_func(None)


print()
from typing import Generator

def my_generator()->Generator[int, None, None]:
    yield 1
    yield
    yield False
    yield lambda a,b:a>b

g = my_generator()
# 使用__next__方法获取生成器的元素
print(g.__next__())  # 1
print(g.__next__())  # None
print(g.__next__()) # False
f = g.__next__()
print(f)  # <function my_generator.<locals>.<lambda> at 0x00000278608D93A0>
print(f(22,11)) # 调用函数，输出： True
# print(g.__next__()) # 如果生成器为空，再取则抛StopIteration异常


from typing import TypeAlias

# Python3.10 版中的新函数
# MyInt = TypeAlias(int, "MyInt")  # 错误用法  TypeError: Cannot instantiate typing.TypeAlias
MyInt: TypeAlias = list[int]
MyInt2: TypeAlias = int

print(type(MyInt), type(MyInt2))  # <class 'types.GenericAlias'> <class 'type'>

num: MyInt2 = 1234
print(type(num), num)  # <class 'int'> 1234

MyType = int
num2: MyType = 12312
print(type(MyType), type(num2), num2)  # <class 'type'> <class 'int'> 12312