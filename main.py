import os
import difflib

print('''
  ______ _____ _      ______       _____ ______          _____   _____ _    _ ______ ____
 |  ____|_   _| |    |  ____|     / ____|  ____|   /\   |  __ \ / ____| |  | |  ____|  __ \ 
 | |__    | | | |    | |__       | (___ | |__     /  \  | |__) | |    | |__| | |__  | |__) |
 |  __|   | | | |    |  __|       \___ \|  __|   / /\ \ |  _  /| |    |  __  |  __| |  _  / 
 | |     _| |_| |____| |____      ____) | |____ / ____ \| | \ \| |____| |  | | |____| | \ \ 
 |_|    |_____|______|______|    |_____/|______/_/    \_\_|  \_\\\_____|_|  |_|______|_|  \_\\

                                        by R4las
\n''')


while True:
    possibleFileName = input('Write below the name of the file:\n')
    possiblePath = input('Write below the folder where you think the file is in:\n')
    
    # controllare se la directory e' valida
    isDir = os.path.isdir(possiblePath) 
    if isDir == False:
        print("Please give me an existing directory folder") 
        continue

    def finder(path, fileName):

        allFilesWithDir = {}
        allFiles = []
        similarFilesString = ''
        
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                allFiles.append(f)
                allFilesWithDir[f] = dirpath
                for key in allFilesWithDir.keys():
                    if key == fileName:
    
                        print(f'File founded at {allFilesWithDir[fileName]}\{key}\n')
                        return

                    similarFilesList = difflib.get_close_matches(fileName, allFiles)
                    similarFilesString = ''
                    similarFilesCounter = 0

                    for element in similarFilesList:
                        similarFilesCounter = similarFilesCounter + 1
                        similarFilesString = similarFilesString + f'{similarFilesCounter} - {allFilesWithDir[element]}\{element}\n'

        print(similarFilesString)

    finder(possiblePath, possibleFileName)