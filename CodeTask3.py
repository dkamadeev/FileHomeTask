File_1 = "1.txt"
File_2 = "2.txt"
File_3 = "3.txt"
File_4 = 'Result.txt'


file_list = [File_1, File_2, File_3]
result_dict = {}

for i in file_list:
    with open(i, encoding='UTF-8') as file_obj:
        list_1 = file_obj.readlines()
        result_dict[i] = list_1

new_list = sorted(result_dict.items(), key=lambda x: len(x[1]), reverse=False)
new_dict = {k: v for k, v in new_list}

def result_1(some_obj):
    for key, value in new_dict.items():
        with open(some_obj, "a", encoding='UTF-8') as file:
            file.write(key + "\n")
            file.write(f'{len(value)}' + "\n")
            count = 0
            for val in value:
                count += 1
                file.write(f'Строка номер {count} файла номер {key}' + "\n")
                file.write(f'{val}' + "\n")
            file.write(f"\n")


result_1(File_4)
