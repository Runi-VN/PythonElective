import webget

#Write a module webget.py that exposes a function to download a file from the web in case it does not exist locally already. 
#The function shall have the following signature download(url, to=None) 
#where the keyword argument to specifies where to save a file locally and with which name. 
#If to == None then the file shall be saved in the current working directory ./ with the same name as it has at its origin. 

#I save to ..\Downloads instead

url = 'https://admin.opendata.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
webget.download_file(url)
# Other directory for testing:
# E:\\pythontestdir\\testname.csv
