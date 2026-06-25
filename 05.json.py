import json

from streamlit import user

#写入json
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "hobby": ["看电影", "看小说", "看游戏"],
}
with open("user.json", "w", encoding="utf-8") as f:
    #ensure_ascii: False 保存中文,默认为True, asc码不能编码中文只能编码字母数字符号
    #indent: 2 缩进(格式化)
    json.dump(user, f, ensure_ascii=False, indent=2)

#读取json文件
with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))