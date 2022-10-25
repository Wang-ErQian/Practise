# 编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上的字样。
# 这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
def make_shirt(size, font):
    """T 恤的尺码和字样"""
    print("T恤的尺码：" + size + "，印花：" + font)

# 使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。


make_shirt('m', '你好')
make_shirt(size='m', font='你好')

