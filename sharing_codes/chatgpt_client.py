# @author:SteveRocket 
# @Date:2023/5/21
# @File:chatgpt_client
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载预训练模型
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2LMHeadModel.from_pretrained('gpt2-medium')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# 定义聊天函数
def chat(text):
    # 将输入文本编码为输入 ID
    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)
    # 使用模型生成输出 ID
    sample_output = model.generate(
        input_ids=input_ids,
        do_sample=True,
        max_length=50,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1
    ).to(device)
    # 解码输出 ID 为文本，并返回
    output = tokenizer.decode(sample_output[0], skip_special_tokens=True)
    return output

# 启动聊天机器人
while True:
    text = input('你: ')
    if text == 'q':
        break
    else:
        reply = chat(text)
        print('聊天机器人:', reply)
