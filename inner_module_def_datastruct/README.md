## inner_constant 内置命名空间

## inner_datastruct 内置数据结构

* list
* tuple
* dict
* set

## inner_except 内置异常

## inner_def 内置函数

* abs()
* all()
* aiter()
* any()
* ascii()
* bin()
* bool()
* bytearray()
* bytes()
* callable()
* chr()
* classmethod()
* compile()
* complex()
* delattr()
* dict()
* dir()
* divmod()
* enumerate()
* eval()
* exec()
* filter()
* float()
* format()
* frozenset()
* getattr()
* globals()
* hasattr()
* hash()
* help()
* hex()
* id()
* input()
* int()
* isinstance()
* issubclass()
* iter()
* len()
* list()
* locals()
* map()
* max()
* memoryview()
* min()
* next()
* object()
* oct()
* open()
* ord()
* pow()
* print()
* property()
* range()
* repr()
* reversed()
* reload()
* round()
* set()
* setattr()
* slice()
* sorted()
* staticmethod()
* str()
* sum()
* super()
* tuple()
* type()
* vars()
* with()
* zip()
* __import__()

#### BLOG

* Python基础之最新的73个内置函数（1）
https://mp.weixin.qq.com/s/F9_G5KjTubhBNtnU_1hr1Q
* Python基础之最新的73个内置函数（2）
https://mp.weixin.qq.com/s/8ownt0SveZQKnsLauP2rOg
* Python基础之最新的73个内置函数（3）
https://mp.weixin.qq.com/s/tKBwtoFyUHhyTuyqs2rGUw
* Python基础之最新的73个内置函数（4）
https://mp.weixin.qq.com/s/Y36qc4Tkw0yQpQyuNdEmTA
* Python基础之最新的73个内置函数（5）
https://mp.weixin.qq.com/s/bsCLCRZBNiT25wOmU1-Kwg
* Python基础之最新的73个内置函数（6）
https://mp.weixin.qq.com/s/jPqx8q2rTG8MtpfZuCVJGw
* Python基础之最新的73个内置函数（7）
https://mp.weixin.qq.com/s/heBcQKNO7Ny1CCerZav__A

## inner_function 内置方法

* `__eq__()`
* `__lt__()`
* `__add__()`
* `__rsub__()`

## inner_module 内置模块（标准库）

1. abc模块

    abc模块 (Abstract Base Classes)是Python标准库中的一个模块，提供了一种抽象基础类的机制。使用抽象基类机制可以帮助开发者定义通用的接口和规范，并通过继承来实现具体的功能。abc模块用于定义和使用抽象基类，让Python实现更加规范和健壮。

2. argparse模块

    argparse模块是Python标准库中的一个模块，提供一种处理命令行参数的方式。开发者可以使用argparse模块来解析命令行参数并生成相应的帮助信息和错误信息，从而使命令行工具更加易用和易于维护。

3. array模块

    array模块是Python标准库中的一个模块，提供了一种基于数组的高效数据类型。使用array模块可以创建和操作数组，从而实现高效的原始数据存储和处理，例如数字、字符、二进制数据等。

4. asyncio模块

    asyncio模块是Python标准库中的一个模块，提供了一种异步IO编程的方式。使用asyncio模块可以轻松地实现异步IO操作，避免阻塞和速度慢的问题，从而提高程序的执行效率和响应速度。

5. base64模块

    base64模块是Python标准库中的一个模块，提供了一种编码和解码二进制数据的方式。使用base64模块可以将二进制数据转换成一种可读的ASCII字符串格式，以便更方便地传输和存储数据。

6. binascii模块

    binascii模块是Python标准库中的一个模块，提供了一种将二进制数据和ASCII码之间互相转换的方式。使用binascii模块可以实现十六进制、二进制和Base64等多种编码和解码操作。

7. builtins模块

    builtins模块是Python标准库中的一个模块，包含了Python内置的函数和异常。Python解释器启动时，builtins模块会自动加载到内存中，使得开发者可以直接使用内置函数和异常而无需导入。

8. bz2模块

    bz2模块是Python标准库中的一个模块，提供了一种对数据进行压缩和解压缩的方式。使用bz2模块可以使用Bzip2算法对数据进行压缩，从而减小数据的大小，节省存储空间和传输带宽。

9. calendar模块

    calendar模块是Python标准库中的一个模块，提供了一种在Python中处理日历的方式。使用calendar模块可以获取并操作日历信息，例如计算日期、星期几和节假日等。

10. cmath模块

    cmath模块是Python标准库中的一个模块，提供了一种支持复数运算的方法。使用cmath模块可以实现复数的加减乘除、三角函数、指数和对数等复杂运算，从而扩展Python的数学计算能力。

11. collections模块

    collections模块是Python标准库中的一个模块，提供了一种使用各种常见数据结构的方式。使用collections模块可以实现一些高级的数据结构，例如有序字典、命名元组、双端队列和计数器等，从而方便地对数据进行处理。

12. configparser模块

    configparser模块是Python标准库中的一个模块，提供了一种读取和写入配置文件的方式。使用configparser模块可以轻松地读取和写入INI格式的配置文件，从而实现程序的配置和参数管理。

13. contextlib模块

    contextlib模块是Python标准库中的一个模块，提供了一种使用上下文管理器的方式。使用contextlib模块可以方便地管理资源，例如文件句柄、网络连接和数据库连接等，从而避免资源泄露和错误。

14. copy模块

    copy模块是Python标准库中的一个模块，提供了一种复制和深度复制对象的方式。使用copy模块可以复制Python对象，包括列表、字典和自定义对象等，从而实现对象的副本和修改。

15. csv模块

    csv模块是Python标准库中的一个模块，提供了一种读写CSV文件的方式。使用csv模块可以轻松地读取和写入CSV格式的文件，从而实现数据的导入和导出。

16. ctypes模块

    ctypes模块是Python标准库中的一个模块，提供了一种调用C语言库的方式。使用ctypes模块可以在Python中直接调用C语言库的函数和变量，从而让Python程序具有调用底层原生代码的能力。

17. dataclasses模块

    dataclasses模块是Python 3.7中新增的一个模块，提供了一种用于定义数据类的方式。使用dataclasses模块可以更简单地定义和创建类，从而提高代码的可读性和可维护性。

18. decimal模块

    decimal模块是Python标准库中的一个模块，提供了一种高精度计算的方式。使用decimal模块可以实现高精度的浮点数计算，避免浮点数运算时产生的精度误差，从而提高计算的准确性。

19. difflib模块

    difflib模块是Python标准库中的一个模块，提供了一种比较文本差异的方式。使用difflib模块可以比较两个文本文件或字符串的差异，并生成差异报告，从而方便地进行版本控制和文本比较。

20. dis模块

    dis模块是Python标准库中的一个模块，提供了一种反汇编Python字节码的方式。使用dis模块可以将Python字节码转换为可读的指令序列，从而分析和优化Python代码。

21. email模块

    email模块是Python标准库中的一个模块，提供了一种处理邮件的方式。使用email模块可以创建和解析邮件，包括邮件头、邮件正文和附件等，从而实现邮件的发送和接收。

22. encodings模块

    encodings模块是Python标准库中的一个模块，提供了一种处理字符编码的方式。使用encodings模块可以实现不同编码格式的转换、编码解码等操作，从而适应不同的字符集和语言环境。

23. enum模块

    enum模块是Python标准库中的一个模块，提供了一种枚举类型的方式。使用enum模块可以创建枚举类型对象，从而实现代码的可读性和可维护性。

24. fileinput模块

    fileinput模块是Python标准库中的一个模块，提供了一种读取多个文件的方式。使用fileinput模块可以方便地读取多个文件并进行处理，从而简化文件输入的代码。

25. fnmatch模块

    fnmatch模块是Python标准库中的一个模块，提供了一种对文件名进行匹配的方式。使用fnmatch模块可以方便地匹配文件名，从而实现文件查找和过滤。

26. functools模块

    functools模块是Python标准库中的一个模块，提供了一些函数式编程工具。使用functools模块可以实现函数的柯里化、偏函数、缓存、包装器等功能，从而提高代码的可读性和可维护性。

27. gc模块

    gc模块是Python标准库中的一个模块，提供了一种垃圾回收机制。使用gc模块可以自动回收不再使用的内存，从而避免内存泄漏和程序崩溃的问题。

28. hashlib模块

    hashlib模块是Python标准库中的一个模块，提供了多种哈希算法。使用hashlib模块可以对数据进行哈希运算，从而得到数据的唯一表示，用于校验数据完整性和加密数据。

29. heapq模块

    heapq模块是Python标准库中的一个模块，提供了一种堆的数据结构。使用heapq模块可以实现排序和查找等操作，从而提高数据处理的效率。

30. hmac模块

    hmac模块是Python标准库中的一个模块，提供了一种基于哈希算法的消息认证码。使用hmac模块可以对消息进行加密和解密，从而保证数据的安全性和完整性。

31. html模块

    html模块是Python标准库中的一个模块，提供了一种操作HTML文档的方式。使用html模块可以解析和生成HTML标记语言，从而实现爬虫和数据处理等应用。

32. http模块

    http模块是Python标准库中的一个模块，提供了一种处理HTTP协议的方式。使用http模块可以发送HTTP请求和处理HTTP响应，从而实现Web应用的开发和测试。

33. imaplib模块

    imaplib模块是Python标准库中的一个模块，提供了一种操作IMAP协议的方式。使用imaplib模块可以连接到邮件服务器，接收和处理邮件，从而实现邮件客户端的开发。

34. imghdr模块

    imghdr模块是Python标准库中的一个模块，提供了一种判断图像文件类型的方式。使用imghdr模块可以判断图像文件的类型，从而方便地进行图像文件的处理和分类。

35. imp模块

    imp模块是Python标准库中的一个模块，提供了一种动态加载模块的方式。使用imp模块可以实现代码的动态加载和执行，从而实现模块化编程。

36. importlib模块

    importlib模块是Python标准库中的一个模块, 提供了一种逆向操作，可以手工构建、分析以及执行 Python 模块，与标准的 import 语句相比更加灵活。

37. inspect模块

    inspect模块是Python标准库中的一个模块，提供了一种对对象进行解析的方式。使用inspect模块可以获取对象的属性、方法和注释等信息，从而实现代码的自省和调试。

38. io模块

    io模块是Python标准库中的一个模块，提供了一种统一的文件、流和编解码等操作方式。使用io模块可以对文本流、二进制流等进行读写操作，并支持编码和解码等功能。

39. itertools模块

    itertools模块是Python标准库中的一个模块，一个创建快速、高效迭代器的模块，提供了一系列用于操作迭代器的工具函数。使用itertools模块可以实现迭代器上复杂的操作，例如排列组合、笛卡尔积、分组和连接等。

40. distutils模块

    distutils模块是Python标准库中的一个模块，用于构建和发布Python程序包。使用distutils模块可以自动完成源代码的编译、安装和发布等过程，从而简化Python程序的开发和发布流程。

41. os模块

    os模块是Python标准库中的一个模块，提供了一种与操作系统交互的方式。使用os模块可以获取文件系统信息、运行外部程序、控制进程和线程、文件操作、目录等操作，与具体的平台无关。

42. sys模块

    sys模块是Python标准库中的一个模块，提供了一些与Python解释器交互的函数和变量。使用sys模块可以获取Python解释器的版本信息、运行时参数、标准输入输出等信息。

43. re模块

    re模块是Python标准库中的一个模块，提供了一种与正则表达式进行操作的方式。使用re模块可以实现字符串的匹配、替换和分割等操作，从而方便文本处理。

44. datetime模块

    datetime模块是Python标准库中的一个模块，提供了一种操作日期和时间的方式。使用datetime模块可以创建日期和时间对象，并进行计算、比较和格式化等操作。datetime模块是对time模块的一个高级封装(time包基于C语言的库函数)。

45. math模块

    math模块是Python标准库中的一个模块，提供了一些常用的数学函数和常量。使用math模块可以进行数学计算、三角函数计算、幂次计算以及后向差分运算等操作。

46. random模块

    random模块是Python标准库中的一个模块，提供了一种生成伪随机数的方式。使用random模块可以生成随机数、随机序列、随机排列等操作，从而实现模拟和随机化处理等功能。

47. pickle模块

    pickle模块是Python标准库中的一个模块，用于序列化和反序列化Python对象。使用pickle模块可以将Python对象转换为二进制格式并存储在文件中，也可以从文件中读入二进制数据并反序列化为Python对象。常用dump()、load()方法。

48. json模块

    json模块是Python标准库中的一个模块，用于处理JSON数据。使用json模块可以将Python对象序列化为JSON格式的字符串，或将JSON格式的字符串反序列化为Python对象。

49. urllib模块

    urllib模块是Python标准库中的一个模块，用于操作URL和HTTP协议。使用urllib模块可以发送HTTP请求、获取响应内容、管理cookie等。

50. socket模块

    socket模块是Python标准库中的一个模块，用于实现网络通信。使用socket模块可以创建TCP、UDP等类型的套接字，并进行网络通信操作，例如发送和接收数据等。

51. time模块

    time模块是Python标准库中的一个模块，用于处理时间和日期。使用time模块可以获取当前时间戳、格式化时间字符串、休眠等待、计算时间差等。

52. subprocess模块

    subprocess模块是Python标准库中的一个模块，用于执行外部命令和程序。使用subprocess模块可以创建子进程、调用外部程序、处理运行时参数等。常用call()、run()、Popen()等方法。

53. shutil模块

    shutil模块是Python标准库中的一个模块，用于文件和目录的高级操作。使用shutil模块可以复制、移动、删除、重命名文件和目录，以及创建压缩文件等。对文件(夹)、压缩包进行处理的模块（移动/复制/打包/解压/修改权限）。

54. hashlib/hmac/uuid模块

    hashlib、hmac和uuid分别是Python标准库中的三个模块，用于进行散列（消息摘要）、消息认证（加密）和UUID（全局唯一标识符）的生成。使用这些模块可以创建散列值、进行信息加密和完整性验证，并生成唯一标识符。

55. configparser模块

    configparser模块是Python标准库中的一个模块，用于解析配置文件。使用configparser模块可以读写INI格式的配置文件，包括节、键和值等信息。

56. threading模块

    threading模块是Python标准库中的一个模块，用于实现多线程编程。使用threading模块可以创建线程、启动线程、管理线程等操作，从而实现多任务并行处理。

57. logging模块

    logging模块是Python标准库中的一个模块，用于实现日志记录。使用logging模块可以配置日志记录器、记录日志信息、格式化日志消息等操作，从而方便程序调试和维护。

58. optparse模块

    optparse模块是Python标准库中的一个模块，用于解析命令行参数。使用optparse模块可以定义命令行参数、解析命令行参数、生成usage信息等操作，从而方便程序的使用和交互。

59. docopt模块

    docopt模块是Python标准库中的一个模块，用于解析命令行参数。使用docopt模块可以根据定义好的命令行参数格式生成帮助信息并解析命令行参数，从而方便程序的使用和交互。

60. operator模块

    operator模块是Python标准库中的一个模块，提供了一些常用的运算操作函数。使用operator模块可以对数字、字符串、列表等对象进行运算操作，例如比较、赋值、逻辑运算等。

61. xml.etree.ElementTree模块

    xml.etree.ElementTree模块是Python标准库中的一个模块，用于解析和生成XML文档。使用xml.etree.ElementTree模块可以读取和写入XML文档、处理XML元素、属性和命名空间等。

62. tempfile模块

    tempfile模块是Pyhon标准库中的一个模块，用于创建临时文件和目录。使用tempfile模块可以创建具有唯一名称的临时文件和目录，从而方便临时文件的处理。

63. timeit模块

    timeit模块是Python标准库中的一个模块，用于测量代码执行时间。使用timeit模块可以测试代码块的执行时间和重复执行次数，从而方便性能优化和程序评估。

64. gzip模块

    gzip模块是Python标准库中的一个模块，它提供了一种压缩和解压缩文件的方式。gzip模块可以读取和写入gzip格式的文件，可以在内存中进行压缩和解压缩操作。

65. zipfile模块

    zipfile模块是Python标准库中的一个模块，它提供了一种压缩和解压缩zip文件的方式。zipfile模块可以读取和写入zip格式的文件，可以在内存中进行压缩和解压缩操作。

66. profile模块

    profile模块是Python标准库中的一个模块，它提供了一种对Python代码进行性能分析的方式。profile模块可以帮助开发者找出代码中的性能瓶颈，从而优化代码的性能。

67. types模块

    types模块是Python标准库中的一个模块，它提供了一些与Python类型相关的常量和函数。types模块中包含了一些内置类型的常量，例如NoneType、FunctionType、GeneratorType等。

68. winreg(Windows)模块

    winreg模块是Python标准库中的一个模块，它提供了一种访问Windows注册表的方式。winreg模块可以读取和写入Windows注册表中的键和值，可以查询注册表中的信息。

69. warnings模块

    warnings模块是Python标准库中的一个模块，它提供了一种处理警告信息的方式。warnings模块可以捕获警告信息并进行处理，例如忽略警告、输出警告信息等。

70. wave模块

    wave模块是Python标准库中的一个模块，它提供了一种读取和写入WAV格式音频文件的方式。wave模块可以读取和写入WAV格式的音频文件，可以获取音频文件的信息，例如采样率、帧率、声道数等。

71. weakref模块

    weakref模块是Python标准库中的一个模块，它提供了一种处理弱引用的方式。weakref模块可以创建弱引用对象，这些对象可以引用其他对象，但不会增加被引用对象的引用计数，从而避免了循环引用的问题。

72. webbrowser模块

    webbrowser模块是Python标准库中的一个模块，它提供了一种打开网页的方式。webbrowser模块可以打开默认浏览器并访问指定的网页，也可以打开指定的浏览器并访问指定的网页。

73. wsgiref模块

    wsgiref模块是Python标准库中的一个模块，它提供了一种实现WSGI（Web Server Gateway Interface）的方式。wsgiref模块可以帮助开发者实现WSGI协议中的应用程序和服务器接口，从而实现Web应用程序。

74. xml模块

    xml模块是Python标准库中的一个模块，它提供了一种处理XML（eXtensible Markup Language）的方式。xml模块可以读取和写入XML格式的文件，可以解析XML文件并生成XML树，可以操作XML树中的节点和属性。

75. xmlrpc模块

    xmlrpc模块是Python标准库中的一个模块，它提供了一种实现XML-RPC（XML Remote Procedure Call）的方式。xmlrpc模块可以帮助开发者实现XML-RPC协议中的客户端和服务器接口，从而实现远程过程调用。

76. zipapp模块

    zipapp模块是Python标准库中的一个模块，它提供了一种将Python应用程序打包成zip文件的方式。zipapp模块可以将Python应用程序打包成一个可执行的zip文件，从而方便地分发和部署应用程序。

77. zipimport模块

    zipimport模块是Python标准库中的一个模块，它提供了一种从zip文件中导入模块的方式。zipimport模块可以从zip文件中加载Python模块，并将其作为普通模块一样使用。

78. zlib模块

    zlib模块是Python标准库中的一个模块，它提供了一种压缩和解压缩数据的方式。zlib模块可以使用DEFLATE算法对数据进行压缩和解压缩，从而减小数据的大小，节省存储空间和传输带宽。

79. shelve模块

    shelve模块是Python标准库中的一个模块，提供了一种简单的方式来使用Python对象持久化存储到文件中，类似于一个小型的数据库。它提供了键值对的方式来存储Python对象。

80. multiprocess模块

    multiprocess模块是Python标准库中的一个模块，它是用来支持并行计算的模块，可以创建多个进程来执行任务。与threading模块不同，multiprocess可以充分利用多核CPU，提高数据处理的效率。

81. atexit模块

    atexit模块是Python标准库中的一个模块，提供了一种注册函数在程序退出时自动运行的方式。使用atexit模块可以在程序退出之前保存数据、关闭文件等操作。

82. concurrent.futures模块

    concurrent.futures模块是Python标准库中的一个模块，提供了一种异步处理的方式。使用concurrent.futures模块可以实现并行计算和非阻塞IO，从而提高数据处理的效率。

83. pstats模块

    pstats模块是Python标准库中的一个模块，提供了一种对Python代码性能分析的方式。使用pstats模块可以统计程序代码的执行时间和函数调用次数等信息，从而优化程序性能。

84. ssl模块

    ssl模块是Python标准库中的一个模块，提供了一种安全套接字层的实现。使用ssl模块可以加密网络连接，从而保证数据的传输安全性。

85. unittest模块

    unittest模块是Python标准库中的一个模块，提供了一种对Python代码进行单元测试的方式。使用unittest模块可以测试代码的正确性和稳定性，从而确保程序的质量。

86. typing模块

    typing模块是Python标准库中的一个模块，提供了一种类型注解的方式。使用typing模块可以对Python变量和函数的参数、返回值等进行类型注解，从而提高代码的可读性和可靠性。

87. zoneinfo模块

    zoneinfo模块是Python标准库中的一个模块，它提供了一种处理时区信息的方式。zoneinfo模块可以获取和操作时区信息，例如获取当前时区、将时间从一个时区转换到另一个时区等。

88. multiprocessing模块

Python标准库中包含了众多模块，涵盖了各种领域，例如文件处理、网络编程、多线程、加密解密、日期时间、数学计算等。掌握Python标准库中的常用模块，可以大大提高编程效率和代码质量，同时也可以拓展自己的编程技能和应用领域。

## inner_type 内置类型


