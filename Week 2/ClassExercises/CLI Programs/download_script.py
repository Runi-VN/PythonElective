import argparse
import webget
#1) Write a program download_script.py, which downloads a set of files from the internet. 
# The files to download are given as arguments to your program on the command-line

# Reuse your webget module from exercises in notebook: 02-0c Modules.

#2) Modify the above program, so that it can download a list of files from stdin. 
# That is, so that you can reuse the output of one CLI command as input to your program.
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a set of URLs and stores it locally.\n Input your URLs as args or with stdin. Use ctrl-z to exit stdin')
    parser.add_argument('url', help='The URL(s) to process', nargs='+', default=[])
    args = parser.parse_args()    
    if not sys.stdin.isatty(): #Checks if a file is connected to stdin
        for url in sys.stdin.read().split('\n'):
            #if not url: break
            print('Downloading from text. Your input:',url)
            webget.download_file(url)
    elif (len(sys.argv) >=2):
        for arg in args.url: #Since we use nargs we always have a list. Nice!
            print('Downloading from args. Your input:',arg)
            webget.download_file(arg)
    else: print('Not satisfied with input method.')
    print('Exiting')
    