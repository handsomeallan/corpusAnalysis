from aip import AipNlp


def isEmoji(content):
    if not content:
        return False
    if u"\uE000" <= content and content <= u"\uE900":
        return True
    if u"\U0001F000" <= content and content <= u"\U0001FA99":
        return True
    else:
        return False

def getBaiduClient():
    APP_ID = '15749954'
    API_KEY = '6x11BXb9P7Z91KCMQulvHt1o'
    SECRET_KEY = 'ni1vyT9G9mo8xUPjWZdrNxUCDtW4D0P3'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    return client

def getParse(str,client):
    #text = "百度是一家高科技公司"

    #'''调用词法分析

    m = client.lexer(str)

    l = []
    for i in range(m['items'].__len__()):
        l.append(m['items'][i]['item']) #取出词法分析中的分词结果
    #'''
    return l

def getPositiveEmo(text,client):
    # '''判断文本情感倾向
    sentimentResult = client.sentimentClassify(text)
    dict = sentimentResult['items'][0]
    return dict['positive_prob']
    # '''

if __name__ == '__main__':

    client = getBaiduClient()

    print(getPositiveEmo('很好',client))

    print(getParse('消息内容',client))


