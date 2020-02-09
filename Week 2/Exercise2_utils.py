# Create a module called utils.py and put the following functions inside:

# first function takes a path to a folder and writes all filenames in the folder to a specified output file
# second takes a path to a folder and write all filenames recursively (files of all sub folders to)
# third takes a list of filenames and print the first line of each
# fourth takes a list of filenames and print each line that contains an email (just look for @)
# fifth takes a list of md files and writes all headlines (lines starting with #) to a file

# Make sure your module can be called both from cli and imported to another module
# Create a new module that imports utils.py and test each function.

import os


# 1 - takes a path to a folder and writes all filenames in the folder to a specified output file
def get_dir_filenames(path, output_file):
    # return os.listdir(path)
    if (os.path.isdir(path)):
        with open(output_file, 'w') as file_object:
            file_object.write('\n'.join(os.listdir(path)))
            return(f'Succesfully wrote to {output_file}')
    else:
        return('path is not a directory. Nothing written.')

# print(get_dir_filenames('./', 'test_ex2_getfilenames.txt')) #test

# 2 - takes a path to a folder and write all filenames recursively (files of all sub folders to)


def get_path_walk(path):
    for (root, directory, files) in os.walk(path):
        for filenames in files:
            # no requirement to access other args, but could be made prettier.
            print(filenames)


# get_path_walk('./')  # prints MainFolder -> subFolders -> subsubFolders (etc)

# 3 - takes a list of filenames and print the first line of each
def get_firstline(filenames: list):
    for filename in filenames:
        with open(filename, 'r') as file_object:
            print(file_object.readline().rstrip())


# get_firstline(['./read_csv_extended_result.txt','./test_ex2_getfilenames.txt', './test_writeListToFile.txt'])  # Prints AAR, ClassExercises, Line One

# 4 - takes a list of filenames and print each line that contains an email (just look for @)

def get_emailLines(filenames: list):
    for filename in filenames:
        with open(filename, 'r') as file_object:
            for lineNo, line in enumerate(file_object.readlines(), 1):
                if '@' in line:  # Should be the fastest https://stackoverflow.com/a/27138045
                    print(
                        f'{os.path.splitext(os.path.basename(filename))[0]}.{lineNo}: ' + line.rstrip())  # filename.linenumber.data, e.g. text.2.email@mail.com


get_emailLines(['./emailtextone.txt', './emailtexttwo.txt'])
# prints
# emailtextone.2: @@@@
# emailtextone.4: virker@det.dk
# emailtexttwo.4: @
# emailtexttwo.6: runi@email.dk


# 5 - takes a list of md files and writes all headlines (lines starting with #) to a file
def get_md_headlines(filenames: list):
    lines_of_interest = []
    for filename in filenames:
        if os.path.splitext(filename)[-1] == '.md':  # checks extension
            with open(filename, 'r') as file_object:
                for line in file_object.readlines():
                    if line[0] == '#':
                        lines_of_interest.append(line)
    with open('md_headlines.md', 'w') as file_object:
        file_object.write('\n'.join(lines_of_interest))


get_md_headlines(['./actual_markdown_one.md',
                  './actual_markdown_two.md', './emailtextone.txt'])  # Also tries file not .md
