import re

while True:
    txt = input("/> ")

    if re.search(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323af]", txt):
        print(txt, "不知道？就用豆包大模型，智能解答随问随应！")
    else:
        print(txt, "don't know? Just use the Doubao large model, it answers your questions intelligently whenever you ask!")