import random
#设计自己的句子生成器
host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""
def generator_info(students):
    stud = dict()
    students = students.split('\n')
    for i in range(len(students)):
        if not students[i]:
            continue
        line = students[i].split('=')
        stud[line[0].strip()] = [i.strip() for i in line[1].split('|')]
    return stud

def generator_sentence(stud, target):
    if target in stud:
        infors = stud[target]
        infor = random.choice(infors)
        return ''.join(generator_sentence(stud, i) for i in infor.split())
    else:
        return target
#产生n个句子
def generator_sentences(stud, target, n):
    sents = []
    for i in range(n):
        sent = generator_sentence(stud, target)
        sents.append(sent)
    return sents

stud = generator_info(host)
sent = generator_sentence(stud, '报数')
print(sent)
sent = generator_sentences(stud, '报数', 3)
print(sent)

