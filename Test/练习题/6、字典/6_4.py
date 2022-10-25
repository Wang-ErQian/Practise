# 既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码，将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
vocabulary = {'vocabulary_1': '1', 'vocabulary_2': '2', 'vocabulary_3': '3', 'vocabulary_4': '4', 'vocabulary_5': '5'}
for key, value in vocabulary.items():
    print("key: " + key + " : "  "value: " + value)
