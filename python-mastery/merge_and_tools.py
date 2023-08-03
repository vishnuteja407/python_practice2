def merge_the_tools(string, k):
    list1 = []
    for i in range(0,len(string),k):
        list1.append(string[i:(i + k)])
    s = ''
    for ele in list1:
        s = ''
        for char in ele:
            if char not in s:
                s += char
        print(s)

                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

