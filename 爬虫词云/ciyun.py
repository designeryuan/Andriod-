import jieba

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('D:/lianxi/stopwordsichun.txt',encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

#给出文档路径
filename = "D:/lianxi/ciyun/chunyu1.txt"
outfilename = "D:/lianxi/ciyun/chunyustop1.txt"
inputs = open(filename, 'r', encoding='UTF-8')
outputs = open(outfilename, 'w', encoding='UTF-8')
#
# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
    print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")

#自定义停用词
file=open("D:/lianxi/ciyun/chunyustop1.txt",encoding='utf-8')
r=file.read()
str=str(r)
r=r.replace('你好','')
r=r.replace('您好','')
r=r.replace('怎么回事','')
print(r)
file=open("D:/lianxi/ciyun/chunyustop1.txt",'w',encoding='utf-8')
for i in r:
    file.write(i)
file.close()


#制作词云
from wordcloud import WordCloud
import jieba

text = open('D:\\lianxi\\ciyun\\chunyustop1.txt', 'r',encoding='utf-8').read()

cut_text = " ".join(jieba.cut(text))

cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path=" D:\lianxi\simhei.ttf",
    collocations=False,
    # font_path=path.join(d,'simsun.ttc'),
    # 设置背景色
    background_color='white',
    # 允许最大词汇
    max_words=200,
    # 最大号字体
    max_font_size=40
)

wCloud = cloud.generate(cut_text)
wCloud.to_file('D:\\lianxi\\chunyu1.png')

import matplotlib.pyplot as plt

plt.imshow(wCloud, interpolation='bilinear')
plt.axis('off')
plt.show()


#词频
# import jieba
# txt = open("D:\\lianxi\\fh.txt", encoding="utf-8").read()
# words  = jieba.lcut(txt)
# counts = {}
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# items = list(counts.items())
# items.sort(key=lambda x:x[1], reverse=True)
# for i in range(30):
#     word, count = items[i]
#     print ("{0:<10}{1:>5}".format(word, count))