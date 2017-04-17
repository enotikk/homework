#функцию, которая удаляет выбранную папку со всеми папками и файлами внутри
import os
def remove_tree(tree):
    for root, dirs, files in os.walk(tree, topdown=False):
        print(root, dirs, files)
        for f in files:
            os.remove(root + os.sep + f)
        for d in dirs:
            os.rmdir(root +os.sep + d)
        os.rmdir(tree)

def main():
    remove_tree(input('Удалить папку: '))

main()
