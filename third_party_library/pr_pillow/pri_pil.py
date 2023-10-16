# @author:SteveRocket 
# @Date:2023/10/1
# @File:pri_pil
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

# 添加一个图片水印,原理就是合并图层，用png比较好

from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, watermark_text, output_path):
    # 打开原始图片
    image = Image.open(image_path)
    # 创建一个新的图像，与原始图片大小相同   这里有一层白色的膜，去掉(255,255,255) 这个参数就好了
    width, height = image.size
    watermark = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 创建一个可绘制的对象
    # draw = ImageDraw.Draw(watermark)  # 在水印层加画笔
    draw = ImageDraw.Draw(watermark, 'RGBA')

    # 设置水印文本的字体和大小
    # font = ImageFont.truetype('arial.ttf', 36)  # 如果没有这个字体的文件  就会乱码，无法正常显示中文
    font = ImageFont.truetype('Deng.ttf', 24)
    # font = ImageFont.truetype('Dengb.ttf', 36)
    # 在水印图像上绘制文本
    i = 0
    while 1:
        sub_height = i * 100
        draw.text((1000, sub_height), watermark_text, font=font, fill=(255, 255, 255, 128))
        i += 1
        if sub_height > height:
            break
    # opacity为透明度

    # angel为角度
    # watermark = watermark.rotate(15, Image.BICUBIC)
    # watermark.rotate(45)

    # 将水印图像叠加到原始图片上
    watermarked = Image.alpha_composite(image.convert('RGBA'), watermark)
    # watermarked = Image.composite(watermark, image, watermark)

    # watermarked.rotate(45)
    # 保存水印图片
    watermarked.save(output_path)


# 测试代码
image_path = r"C:\Users\rocke\Desktop\Articulate2.0.png"  # 原始图片路径
watermark_text = u'微信公众号：CTO Plus'  # 水印文本
output_path = 'Articulate2.0.png'  # 输出图片路径

add_watermark(image_path, watermark_text, output_path)
