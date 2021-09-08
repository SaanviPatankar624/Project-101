import os
import dropbox
from dropbox import dropbox_client
from dropbox.files import WriteMode

class TransferData():
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                localpath = os.path.join(root,file_name)
                relativepath = os.path.relpath(localpath,file_from)
                dropboxpath = os.path.join(file_to, relativepath)
                with open (localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxpath, mode=WriteMode('overwrite'))
        
def main():
    access_token = "sSfrjcEz1WkAAAAAAAAAAaD0tqhXT8CGMugEZ2Qyj8B51RyRinizeswOHj-o1W3gtx"
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("enter the full path to upload to dropbox")

    transferData.upload_files(file_from, file_to)
    print("file has been moved sucessfully")

main()


            



