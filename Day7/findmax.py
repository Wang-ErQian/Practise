"""
找出列表中最大或最小的元素
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的函数max和min找出列表中最大和最小元素
    print(max(fruits))
    print(min(fruits))
    
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        if fruits[index] < min_value:
            min_value = fruits[index]
    print('Max：', max_value)
    print('Min：', min_value)
    
if __name__ == '__main__':
    main()