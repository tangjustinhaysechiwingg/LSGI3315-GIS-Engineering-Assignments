# LSGI3315 Lab 2 20016345D Example 4 - Variable-length Arguments (Keyword)
def generate_list(**kwargs):
    # items() allows you to iterate through each key-value
    new_list = []

    for key, value in kwargs.items():
        new_list.append([key, value])
    return new_list


if __name__ == '__main__':
    list1 = generate_list(Barry=1500, Wallace=2800)
    list2 = generate_list(Sammy=8000, Jeffrey=9220, Justin=5000)
    print('list 1:', list1)
    print('The first record in list 1:', list1[0])
    print('list 2:', list2)
    print('The second record in list 1', list2[2])
