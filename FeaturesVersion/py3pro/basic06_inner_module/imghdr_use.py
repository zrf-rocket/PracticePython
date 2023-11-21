import os
import imghdr

def check_img_type():
    path = r"C:\Users\Administrator\Desktop\imgs"
    for img in os.listdir(path=path):
        try:
            img_file = path + os.sep + img
            if os.path.isfile(img_file):
                img_type = imghdr.what(img_file)
                if img_type is not None:
                    print('The image type is: ', img_type)
                else:
                    print('The file is not an image.')
        except Exception as e:
            print(e)


def check_file_datastream():
    files = [
        r"C:\Users\Administrator\Desktop\imgs\test.txt",  # The data is not an image.
        r"C:\Users\Administrator\Desktop\imgs\Python.png"  # The image type is:  png
    ]
    for file in files:
        with open(file, 'rb') as img_file:
            img_type = imghdr.what(None, h=img_file.read())
            if img_type is not None:
                print('The image type is: ', img_type)
            else:
                print('The data is not an image.')


filename = r"C:\Users\Administrator\Desktop\imgs\Python.png"
# imghdr.what()可以接收一个文件路径，也可以接收一个文件对象。输出一个文件类型
img_type = imghdr.what(filename)

if img_type is not None:
    print('The image type is: ', img_type)
else:
    print('The file extension is not an image.')



import imghdr
import requests
# https://t7.baidu.com/it/u=2511982910,2454873241&fm=193&f=GIF
reponse = requests.get('https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF')
type = imghdr.what(None, reponse.content)
print(type)
with open('1.'+type,'wb') as f:
    f.write(reponse.content)
