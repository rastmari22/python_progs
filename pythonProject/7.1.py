def getRES(filename):
    for i in filename:
        try:
            with open(f'{i}') as f:
                with open('RES.TXT','a') as res_file:
                    res_file.write(f.read())
                    print(f"Файл {i} записан в файл RES.txt")
        except FileNotFoundError:
            return print('ошибка')
    return 'RES.txt'

file_names=['F123.TXT','F134.TXT','F135.TXT',]

with open(getRES(file_names)) as res:
    print(res.read())