"""
定义和使用字典
"""


def main():
    scores = {'王': 95, '二': 78, '千': 82}
    print(scores['王'])
    print(scores['千'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['二'] = 65
    scores['陈'] = 71
    scores.update(瑞 = 67, 东 = 85)
    print(scores)
    if '西' in scores:
        print(scores['西'])
    print(scores.get('西'))
    print(scores.get('西', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('王', 100))
    print(scores)
    scores.clear()
    print(scores)
    
    
    
if __name__ == '__main__':
    main()