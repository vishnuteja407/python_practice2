def count_words(file_path):
    with open(file_path, 'r') as f_read:
        data = f_read.read()
        result = data.split(" ")
        return len(result)

func = count_words('words1.txt')
print(func)