"""
jsonpath表达式的基本格式规范：
  $ 表示根节点，也是所有jsonpath表达式的开始
  . 表示获取子节点
  .. 表示获取所有符合条件的内容
  *  代表所有的元素节点
  [] 表示迭代器的标示（可以用于处理下标等情况）
  [,] 表示多个结果的选择
  ?() 表示过滤操作
  @ 表示当前节点
"""
import jsonpath

json1 = {
    "name": "John",
    "age": 30
}
# print(jsonpath.jsonpath(json1, '$.name'))


from jsonpath import jsonpath

json2 = {
    "students": [
        {
            "name": "John",
            "age": 30
        },
        {
            "name": "Mary",
            "age": 25
        }
    ]
}
# print(jsonpath(json2, '$[0]'))
# print(jsonpath(json2, '$.students[0]'))

json3 = [
    {
        "name": "John",
        "age": 30
    },
    {
        "name": "Mary",
        "age": 25
    }
]
# print(jsonpath(json3, '$[0]'))


json4 = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "555-1234"
        },
        {
            "type": "work",
            "number": "555-5678"
        }
    ]
}

# print(jsonpath(json4, '$'))
# print(jsonpath(json4, '$.address.city'))
# print(jsonpath(json4, '$.phoneNumbers[0].number'))
# print(jsonpath(json4, '$.phoneNumbers[*].type'))

print(jsonpath(json4, '$.phoneNumbers[0]'))
print(jsonpath(json4, '$.phoneNumbers.*.number | length(@)'))
print(jsonpath(json4, '$.phoneNumbers.*.number.length()'))
# print(jsonpath(json4, '$..phoneNumbers | length(@)'))
# print(jsonpath(json4, '$...phoneNumbers.*.number'))
# print(jsonpath(json4, '$...phoneNumbers.*.number | length(@)'))


json5 = {
    "name": [
        {
            "username": "reference",
            "age": 25
        },
        {
            "username": "reference",
            "age": 30
        }
    ]}
# print(jsonpath(json5, '$.name[?(@.age > 25)]'))


data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}



# 基于JsonPath获取元素：通过jsonpath函数来获取（json数据，定位表达式）
bike = jsonpath(data, '$.store.bicycle.color')
print(bike)
print(bike[0])
book = jsonpath(data, '$.store.book')
print(book)

# 获取store下所有的price节点的值
price = jsonpath(data, '$.store..price')
print(price)

# 连接操作符，在xpath中 结果合并其他结果的集合。JSONPATH允许name或者数据索引。类似于xpath |
book_price = jsonpath(data, '$.store.book[0,1,2].price')

# 切片遵循list的切片规则
book_price1 = jsonpath(data, '$.store.book[0:3].price')
print(book_price)
print(f'book_price1:{book_price1}')

# 获取price大于10的所有book
book_1 = jsonpath(data, '$..book[?(@.price>10)]')
print(book_1)

# 这是一条错误的JsonPath
book_2 = jsonpath(data, '$..WHOAMI[?(@.price>10)]')
print(book_2)
print(type(book_2))
print(type(data))
