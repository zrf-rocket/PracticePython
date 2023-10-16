# @author:SteveRocket 
# @Date:2023/10/1
# @File:filetools_demo
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def watermark_Image(img_path, output_path, text, pos):
    img = Image.open(img_path)
    drawing = ImageDraw.Draw(img)
    black = (255, 255, 255)
    font = ImageFont.truetype('arial.ttf', 36)
    drawing.text(pos, text, font=font, fill=black)
    img.show()
    img.save(output_path)


img = r"C:\Users\rocke\Desktop\Articulate2.0.png"  # 原始图片路径
watermark_Image(img, 'Articulate2.0.png', 'CTO Plus', pos=(10, 10))
# watermark_Image(img, 'Articulate2.0.png', '微信公众号：CTO Plus', pos=(10, 10))