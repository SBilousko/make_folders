import os, os.path

# Глобальный путь к папке с проектом (в которой создается дерево папок, получаем у пользователя)
path = os.path.dirname(__file__)

# Имя проекта (корневой папки для дерева, получаем у пользователя)
projectName = 'test'

foldersList = 'foldersList.txt'
foldersListPath = os.path.join(path, foldersList)

# Текущая корневая папка = корневой папке проекта
rootFolder = projectRoot = os.path.join(path, projectName)

sp = 0

def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

file = open(foldersListPath, 'r')

for f in file:
    if f.find('#') != -1:
        continue
    elif not f.startswith(' '):
        sp = 0
        path = rootFolder = projectRoot + r'/' + f.strip()
        createFolder(path)
    elif f.startswith(' '):
        i = 0
        for ch in f:
            if ch.find(' ') == -1:
                break
            i = i + 1
        if i > sp:
            sp = i
            path = rootFolder = rootFolder + r'/' + f.strip()
            createFolder(path)
        elif i == sp:
            rootFolder = rootFolder[:rootFolder.rfind(r'/')]
            path = rootFolder = rootFolder + r'/' + f.strip()
            createFolder(path)
        elif i < sp:
            j = (sp - i)/2 + 1
            while j >= 1:
                rootFolder = rootFolder[:rootFolder.rfind(r'/')]
                j = j - 1
            path = rootFolder = rootFolder + r'/' + f.strip()
            createFolder(path)
            sp = i

file.close()