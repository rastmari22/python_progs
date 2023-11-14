import os, sys, shutil, psutil
def list_files_in_directory():
    print(os.listdir())


def info_about_system():
    print("Количество процессоров:", psutil.cpu_count(logical=False))
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Текущая директория:", os.getcwd())
    print("Логин пользователя:", os.getlogin())

def list_running_processes():
    for proc in psutil.process_iter(['pid', 'name']):#'username
        print(proc.info)

def duplicate_all_files():
    # files = os.listdir(".")
    for file in os.listdir():
        shutil.copy(file, file+"_copy")

def duplicate_specific_file(filename):
    shutil.copy(filename, filename+"_copy")

def delete_duplicate_files():
    exists_file = set()
    for file in os.listdir():
        if file not in seen:
            exists_file.add(file)
        else:
            os.remove(file)

def delete_empty_directories():
    for root, dirs, files in os.walk(".", topdown=False):#первыми будут подкаталоги).
        print(root,dirs,files)
        for directory in dirs:
            if not os.listdir(os.path.join(root, directory)):#полный адрес файла
                os.rmdir(os.path.join(root, directory))

def delete_specific_file_type(ft):
    for file in os.listdir():
        if file.endswith(ft):
            os.remove(file)


def rename_specific_file(old_name, new_name):
    os.rename(old_name, new_name)



def main():
    while True:
        print("\nМеню:")
        print("1. Вывести список файлов в текущей директории")
        print("2. Вывести информацию об операционной системе")
        print("3. Вывести список всех работающих процессов")
        print("4. Дублировать все файлы в текущей директории")
        print("5. Дублировать конкретный файл")
        print("6. Удалить дубликаты файлов из директории")
        print("7. Удалить пустые директории")
        print("8. Удалить файлы определенного типа")
        print("9. Переименовать конкретный файл")
        print("0. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            list_files_in_directory()
        elif choice == '2':
            info_about_system()
        elif choice == '3':
            list_running_processes()
        elif choice == '4':
            duplicate_all_files()
        elif choice == '5':
            filename = input("Введите имя файла для дублирования: ")
            duplicate_specific_file(filename)
        elif choice == '6':
            delete_duplicate_files()
        elif choice == '7':
            delete_empty_directories()
        elif choice == '8':
            extension = input("Введите тип удаляемых файлов: ")
            delete_specific_file_type(extension)
        elif choice == '9':
            old_name = input("Введите текущее имя файла: ")
            new_name = input("Введите новое имя файла: ")
            rename_specific_file(old_name, new_name)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор")

main()
