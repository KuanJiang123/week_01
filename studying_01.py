import random
from collections import Counter
import jieba
hello_relus = '''
say_hello = names hello tail
names = name names | name
name = Jhon | Mike | 老梁　｜　老刘
hello = 你好 | 你来了 | 快请进
tail = ya | !
'''
def generate(grammar_str, target):
    if target in grammar_str:
        candidates = grammar_str[target]
        candidate = random.choice(candidates)

        return ''.join(generate(grammar_str, target=c.strip()) for c in candidate.split())
    else:
        return target

def get_generation_by_gram(grammar_str : str, target, stmt_split='=', or_split='|'):
    rules = dict()
    for line in grammar_str.split('\n'):
        if not line: continue
        stmt, expr = line.split(stmt_split)
        rules[stmt.strip()] = expr.split(or_split)
    generated = generate(rules, target=target)
    return generated

sentences = '此外自本周6月12日起除小米手机6等15款机型外其余机型已暂停更新发布含开发版体验版内测稳定' \
            '版暂不受影响以确保工程师可以集中全部精力进行系统优化工作有人猜测这也是将精力主要用到MIUI9的研发' \
            '之中MIUI8去年5月发布距今已有一年有余也是时候更新换代了当然关于MIUI9的确切信息我们还是等待官方消' \
            '息\n骁龙835作为唯一通过Windows10桌面平台认证的ARM处理器高通强调不会因为只考虑性能而去屏蔽掉小核' \
            '心相反他们正联手微软找到一种适合桌面平台的兼顾性能和功耗的完美方案报道称微软已经拿到了一些新的源码' \
            '以便Windows10更好地理解biglittle架构资料显示骁龙835作为一款集成了CPUGPU基带蓝牙WiFi的SoC比传统' \
            '的Wintel方案可以节省至少30的PCB空间按计划今年Q4华硕惠普联想将首发骁龙835Win10电脑预计均是二合' \
            '一形态的产品当然高通骁龙只是个开始未来也许还能见到三星Exynos联发科华为麒麟小米澎湃等进入Windows1' \
            '0桌面平台\n此前的一加3T搭载的是3400mAh电池DashCharge快充规格为5V4A至于电池缩水可能与刘作虎所说' \
            '一加手机5要做市面最轻薄'

def get_gram_count(word, wc):
    if word in wc: return wc[word]
    else:
        return wc.most_common()[-1][-1]

TOKENS = list(jieba.cut(sentences))
print(len(TOKENS))

_2_gram_words = [
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]
_2_gram_word_counts = Counter(_2_gram_words)
words_count = Counter(jieba.cut(sentences))
def two_gram_model(sentence):
    # 2-gram langauge model
    tokens = list(jieba.cut(sentence))

    probability = 1

    for i in range(len(tokens) - 1):
        word = tokens[i]
        next_word = tokens[i + 1]

        _two_gram_c = get_gram_count(word + next_word, _2_gram_word_counts)
        _one_gram_c = get_gram_count(word, words_count)
        pro = _two_gram_c / _one_gram_c

        probability *= pro

    return probability


print(two_gram_model('前天早上吃晚饭的时候'))







