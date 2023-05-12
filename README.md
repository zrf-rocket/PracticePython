# Python

主要基于Python3.11。以及Python2/3.6、3.8、3.10、3.11各自版本的特性。

## 涉及内容：

### 不同版本新增的特性

### Python开发技巧

#### 错误和异常处理

* 将输出用日志记录到文件中
* 处理多个异常
* 捕获所有异常
* 创建自定义异常
* 捕获异常后抛出另外的异常
* 重新抛出最后的异常
* 输出警告信息
* 调试基本的程序崩溃错误

### 基本特性

### py2与py3的区别

### 高级特性

#### 推导式

是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体，支持各种数据结构的推导式：

* 列表(list)推导式
* 字典(dict)推导式
* 集合(set)推导式
* 元组(tuple)推导式

### 性能调优

### 底层原理

### 内置库、内置方法、第三方库

### 面向对象
#### 函数
<pre>
  函数对象是通过函数定义创建的。 对函数对象的唯一操作是调用它: func(argument-list)。
  实际上存在两种不同的函数对象：内置函数和用户自定义函数。 两者支持同样的操作（调用函数），但实现方式不同，因此对象类型也不同。
</pre>

#### 方法
<pre>
  方法是使用属性表示法来调用的函数。 存在两种形式：内置方法（例如列表的 append() 方法）和类实例方法。 内置方法由支持它们的类型来描述。
  如果你通过一个实例来访问方法（即定义在类命名空间内的函数），你会得到一个特殊对象: 绑定方法 (或称 实例方法) 对象。 当被调用时，它会将 self 参数添加到参数列表。 绑定方法具有两个特殊的只读属性: m.__self__ 操作该方法的对象，而 m.__func__ 是实现该方法的函数。 调用 m(arg-1, arg-2, ..., arg-n) 完全等价于调用 m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)。
  与函数对象类似，绑定方法对象也支持获取任意属性。 但是，由于方法属性实际上保存于下层的函数对象中 (meth.__func__)，因此不允许设置绑定方法的方法属性。 尝试设置方法的属性将会导致引发 AttributeError。 想要设置方法属性，你必须在下层的函数对象中显式地对其进行设置:
</pre>

### 网络编程

### 设计模式

### 数据结构

### 算法

### 安全编程

### 开发框架

### 自动化测试框架

### 机器学习

### 科学计算

### 开发规范

### 安全规范

## python开发环境

### 虚拟环境

* virtualenv
* pipenv
* anaconda

### pip

* 包名
    * pip install package_name
* 包文件
    * pip install package_name.whl/package_name.tar.gz
* 文件包清单
    * pip install -r requirements.txt
* 添加源
    * pip install -r requirements.txt -i resource_url

### 目录

#### 3.8ch Python3.10的新特性

    *

#### 3.10ch Python3.10的新特性

    *

#### 3.11ch Python3.11的新特性

    *

#### [inner_module_def_datastruct 内置模块、内置函数、内置数据结构](./inner_module_def_datastruct/README.md)

* inner_constant 内置常量
* inner_datastruct 内置数据结构
* inner_def 内置函数
* inner_except 内置异常
* inner_module 内置模块
* inner_type 内置类型

#### performance_implementation

* development_skills 开发技巧
* implementation 实现原理
* performance 性能特性

#### third_party_library 第三方库

* pr_airflow
* pr_apscheduler
* pr_celery
* pr_consul
* pr_elasticsearch
* pr_influxdb-client
* pr_kafka
* pr_mysql
* pr_open_cv
* pr_redis
* pr_sqlarchmy
* pr_whatchdog
* pr_pyaudio
* pr_jsonschema
* pr_pyaudio
* 
* [sklearn](https://www.sklearncn.cn/)


## 引申

* [Python常用的主流开发框架 Python Framework](https://gitee.com/SteveRocket/python_framework)
* [Python常用的自动化测试框架 Python Automation(Unittest) Framework](https://gitee.com/SteveRocket/python_test_automation_framework)
* [Python各版本特性标准库文档](https://docs.python.org/zh-cn/3/)







