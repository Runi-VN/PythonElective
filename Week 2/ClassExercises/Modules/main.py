import webget

url = 'https://admin.opendata.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
webget.download_file(url)
# Other directory for testing:
# E:\\pythontestdir\\testname.csv
