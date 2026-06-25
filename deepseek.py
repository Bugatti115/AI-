import os
from openai import OpenAI

# 从环境变量读取 API Key（更安全）
api_key = os.environ.get('DEEPSEEK_API_KEY')
if not api_key:
    print("错误: 请设置 DEEPSEEK_API_KEY 环境变量")
    exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

try:
    response = client.chat.completions.create(
        model="deepseek-chat",  # 建议改成正确的模型名
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "你好"}
        ],
        stream=False
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"错误: {e}")