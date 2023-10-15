# @author:SteveRocket 
# @Date:2023/6/18
# @File:pyttsx3_use
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 350)  # 设置语速，默认 200，数值越大语速越快
engine.setProperty('volume', 1) # 设置音量，默认值是`1`，可以调整为`0`到`1`之间的值，数值越大音量越大。

voices = engine.getProperty('voices')
for i in voices:
    print(i)

# engine.setProperty('voice', voice_id)
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0')
# engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
live_contents = ""
with open('./static/voices.txt', encoding='utf-8') as to_live:
    live_contents = to_live.read()
# engine.say('爱我中华')
engine.say(live_contents)
engine.runAndWait() # 等待结束








