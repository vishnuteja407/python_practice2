import textwrap

def wrap(string, max_width):
    data = ''
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    for element in word_list:
        data = data + element + "\n"
    return data

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)