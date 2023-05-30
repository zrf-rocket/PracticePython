# aiter() 的作用、特性以及详细用法
# 1. 作用
# aiter()函数用于获取异步可迭代对象的迭代器，异步可迭代对象是一种支持异步迭代的对象，它的__aiter__()方法返回一个异步迭代器。

# 2. 特性
# - aiter()函数的参数必须是异步可迭代对象。
# - aiter()函数返回一个异步迭代器对象。
# - 异步迭代器是一种支持异步迭代的对象，它的__anext__()方法返回一个异步可等待对象，当异步可等待对象完成时，返回下一个值。


# anext() 的作用、特性以及详细用法
# 1. 作用
# anext()函数用于获取异步迭代器的下一个值。异步迭代器是一种支持异步迭代的对象，它的__anext__()方法返回一个异步可等待对象，当异步可等待对象完成时，返回下一个值。
#
# 2. 特性
# - anext()函数的参数必须是异步迭代器对象。
# - anext()函数返回一个异步可等待对象，当异步可等待对象完成时，返回下一个值。
# - 如果异步迭代器没有下一个值，anext()函数会抛出StopAsyncIteration异常。

import asyncio
from inner_module_def_datastruct import WEIXIN_URL
async def async_generator():
    for i, e in enumerate(WEIXIN_URL):
        yield i, e
        await asyncio.sleep(1)

async def main():
    async for i in async_generator():
        print(i)

async def test():
    async_iter = async_generator().__aiter__()
    while True:
        try:
            # value = await async_iter.__anext__()
            value = await asyncio.wait_for(async_iter.__anext__(), timeout=1)
            print(value)
        except StopAsyncIteration:
            break
        except asyncio.TimeoutError:
            print('Timeout')

asyncio.run(main())
asyncio.run(test())

# 此示例我们定义了一个异步生成器async_generator()，它每隔1秒钟产生一个数字，并使用async for循环和异步生成器进行异步迭代。
# 我们还定义了一个test()函数，使用aiter()函数获取异步可迭代对象的迭代器，并使用anext()函数逐个获取异步生成器产生的数字，如果等待时间超过1秒钟，会抛出TimeoutError异常。