# 修改函数 make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号 T 恤。
# 调用这个函数来制作如下 T 恤：一件印有默认字样的大号 T 恤、一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）
def make_shirt(size='L', font='I love Python'):
    """T 恤的尺码和字样"""
    print("T恤的尺码：" + size + "，印花：" + font)


make_shirt('L')
make_shirt('M')
make_shirt(font='123456')