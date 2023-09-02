import sys 


for line in sys.stdin:
    word_list = line.split(',')
    # 每个单词和逗号之间总字符数
    total_char_num = 10

    for word in word_list[:-1]:
        # 使用格式化,指定占位符宽度为总字符数
        print('{:{}},'.format(word, total_char_num), end='')

    print(word_list[-1], end='')
