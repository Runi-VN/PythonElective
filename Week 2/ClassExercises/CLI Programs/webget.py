import os
import urllib.request as req
from urllib.parse import urlparse

#Copy of webget. cant import submodule

def download_file(url, to=None):
    """Download a remote file specified by a URL to a
      local directory. Default location is <working directory>\Downloads\<filename>

      :param url: str
          URL pointing to a remote file.

      :param to: str
          Local path, absolute or relative, with a filename
          to the file storing the contents of the remote file.
      """
    url_parsed = urlparse(url)
    filename = os.path.basename(url_parsed.path) #also holds extension
    local_file = os.path.isfile(to if to else "..\\Downloads" + "\\" + filename)
    #print('URL_PARSED:', url_parsed)
    #print('Filename: ', filename)
    #print('local_file at {path} exists: {file_check}'.format(path=(to if to else os.path.abspath("..\\Downloads\\"+ filename)), file_check=local_file))
    if to and os.path.isfile(to) or local_file: #if file exists at {to} or defaultdirectory
        print(f'File {filename} already exists.\nParameters: url={url}, to={to}\nExiting. ')
    else:
        if to: save_location = to
        else: save_location = r"..\Downloads" + "\\" + filename
        #print('save_location: ' + save_location)
        print('Attempting to retrieve file...')
        downloaded_file = req.urlretrieve(url, save_location)
        if downloaded_file: print('Saved file at: ' + downloaded_file[0])
        #open with(save_location,"w").write(downloaded_file)