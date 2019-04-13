import jieba, codecs, math
import jieba.posseg as pseg

names = {}
relationships = {}
lineNames = []

# count names
jieba.load_userdict("data/dict.txt")
with codecs.open("data/data.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if w.flag != "nr" or len(w.word) < 1:
                continue
            print("赋值前：")
            print(lineNames[-1])
            lineNames[-1].append(w.word)
            print("赋值后：".format(lineNames[-1]))
            print(lineNames[-1])
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1
# explore relationships

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1

# output
with codecs.open("data/node.txt", "w", "utf8") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("data/edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")

print(names)