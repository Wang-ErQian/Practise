# 访问项目Gutenberg（http://gutenberg.org/），并找一些你想分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。
# 例如，下面的代码计算'row'在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用lower()将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg 中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。
with open('../../pg68498.txt') as obj_file:
    im_word = obj_file.read()
    count_the = im_word.lower().count('the')
    print(count_the)

