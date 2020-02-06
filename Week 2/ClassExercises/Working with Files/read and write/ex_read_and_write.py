import os

#1. create a function in python, that can read all names of files in a folder, when given the full path to the folder

def getFiles(dirpath):
    return os.listdir(dirpath)

#2. create a function, that can read all lines from a file and copy to another file only the lines, that starts with a number

def getFileLinesWithLeadingDigit(file_path):
    linesOfInterest = []
    with open(file_path) as file_object:
        #print(newfilename)
        for line in file_object:
            if line[0].isdigit(): linesOfInterest.append(line)
    #print(linesOfInterest)
    # Set up new file
    basename = os.path.basename(file_path) #filename.extension
    splitname = os.path.splitext(basename) #split into filename, extension
    file_directory = os.path.dirname(file_path) #get current file path
    newfilepath = file_directory + '\\' + splitname[0] + '_leadingDigits' + splitname[1] #text.txt turns into text_leadingDigits.txt
    
    #print(newfilepath)
    if not linesOfInterest:
        return('no lines starting with digits')
    else:
        with open(newfilepath, 'w') as file_object:
            for line in linesOfInterest:
                file_object.write(line)
    return('done finding digits, see your file at:\n' + newfilepath)

    

#3. create a function that can read all files in folder 
# and all subfolders and print a list of all png files including their full path name
def getPNG(path):
    pathsOfInterest = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".png"):
                pathsOfInterest.append(os.path.join(root, name))
    if not pathsOfInterest:
        return('error: no PNGs')
    else:
        return pathsOfInterest

            