# -*-coding:utf-8-*-


import os
"""
    合并文本文件
"""
mergefiledir = os.getcwd()+'\\stopwords'
filenames = os.listdir(mergefiledir)
file = open('stopwords.txt', 'w')

for filename in filenames:
    filepath = mergefiledir + '\\' + filename
    for line in open(filepath):
        file.writelines(line)
    file.write('\n')

"""
    去重
"""
lines = open('stopwords.txt', 'r')
newfile = open('stopword.txt', 'w')
new = []
for line in lines.readlines():
    if line not in new:
        new.append(line)
        newfile.writelines(line)

file.close()
newfile.close()
