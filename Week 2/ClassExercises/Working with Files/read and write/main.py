import ex_read_and_write as ex1
import os
# Used for testing exercises

print(ex1.getFiles('C:\\'))

print(ex1.getFileLinesWithLeadingDigit(os.getcwd() + '\\some_with_digits.txt'))

for image_path in ex1.getPNG(os.getcwd()):
    print(image_path)