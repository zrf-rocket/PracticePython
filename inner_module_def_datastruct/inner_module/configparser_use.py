import configparser

def read_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read('config.ini')

    # 获取配置项的值
    db_host = config.get('database', 'host')
    db_port = config.getint('database', 'port')
    db_username = config.get('database', 'username')
    db_password = config.get('database', 'password')
    db_database = config.get('database', 'database')
    web_host = config.get('web', 'host')
    web_port = config.getint('web', 'port')
    web_debug = config.getboolean('web', 'debug')
    weixin_url = config.get('url', 'WEIXIN_URL')
    csdn_url = config.get('url', 'CSDN_URL')
    git_url = config.get('url', 'GIT_URL')

    # 打印配置项的值
    print('database.host:', db_host)
    print('database.port:', db_port)
    print('database.username:', db_username)
    print('database.password:', db_password)
    print('database.database:', db_database)
    print('web.host:', web_host)
    print('web.port:', web_port)
    print('web.debug:', web_debug)
    print('weixin_url:', weixin_url)
    print('csdn_url:', csdn_url)
    print('git_url:', git_url)



import configparser

def create_file():
    # 创建ConfigParser对象
    config = configparser.ConfigParser()
    # 设置配置项的值
    config['database'] = {
        'host': 'localhost',
        'port': 3306,
        'username': 'root',
        'password': '123456',
        'database': 'test_db'
    }
    config['web'] = {
        'host': '127.0.0.1',
        'port': 8080,  # 此处的数字可以不用引号
        'debug': True  # 此处的True可以不用引号
    }
    config['url'] = {
        'CSDN_URL': "https://blog.csdn.net/zhouruifu2015/",
        'WEIXIN_URL': "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q",
        'GIT_URL': "https://gitee.com/SteveRocket/practice_python.git"
    }
    # 写入配置文件
    with open('config02.ini', 'w') as f:
        config.write(f)
    print('写入完成')

