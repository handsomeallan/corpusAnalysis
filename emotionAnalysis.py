import jieba
import baiduAip
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码

# 1 分词

# 分词并去停用词
def readLines(fileName):
    f = open(fileName,'r',encoding = 'utf-8-sig')
    result = []
    for s in f:
        result.append(s)
    f.close()
    return result

def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)

    stopwords = readLines('data/stop_words.txt')
    stopWords = []
    for s in stopwords:
        stopWords.append(s.replace('\n',''))
    # print(stopWords)
    newSent = []
    for word in segResult:
        if word in stopWords:
            #print("stopword: %s" % word)
            continue
        else:
            newSent.append(word)

    return newSent
# def strdecode(sentence):
#     if not isinstance(sentence, str):
#         try:
#             sentence = sentence.decode('utf-8')
#         except UnicodeDecodeError:
#             sentence = sentence.decode('gbk', 'ignore')
#     return sentence
def isEmoji(content):
    if not content:
        return False
    if u"\uE000" <= content and content <= u"\uE900":
        return True
    if u"\U0001F000" <= content and content <= u"\U0001FA99":
        return True
    else:
        return False
if __name__ == '__main__':

    f = readLines("data/data.txt")
    client = baiduAip.getBaiduClient()

    wordList = []
    # 获得句子情感倾向
    for line in f:
        try:
            e = baiduAip.getPositiveEmo(line, client)
            print(line,e)
        except:
            print(line,0)
        # 利用百度aip分词
        #wordList = sent2word(line)
        # print(type(line))
        #print(line)
        #strdecode(line)
        # i = 0
        # while i < len(line):
        #     s = line[i]
        #     if isEmoji(s):
        #         try:
        #             line = line[:i-1]+line[i+1:]
        #         except:
        #             line = ''
        #     i+=1
        # try:
        #     wordList = baiduAip.getParse(line,client) # 原纪录中含有类似于：\U0001f451这种Unicode格式的字符串，无法处理，必须提前处理
        #     print(wordList)
        # except:
        #     print(line)
