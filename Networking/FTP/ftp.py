#FTP example program to access files on a server

from ftplib import FTP

def ftp_connect(server, username='', password=''):
    ftp = FTP(server)
    ftp.login(username, password)
    return ftp

ftp = ftp_connect("ftp.nluug.nl", "anonymous", "ftplib-example-1")

#example commands to move directory and copy files
ftp.cwd('pub/')
ftp.retrlines('LIST')
ftp.retrbinary('RETR README.nluug', open('Networking/READMEcopyTest', 'wb').write)
ftp.quit()

def get_file():

    filename = 'example.txt' # remote server file to be copied
    localfile = open(filename + 'copy', 'wb') # local version of file 
    ftp.retrbinary('RETR ' + filename, localfile.write) # copy the remote to local

    ftp.quit()
    localfile.close()

def push_file():

    filename = 'exampleFile.txt' # local file name
    ftp.storbinary('STOR ' + filename, open(filename, 'rb')) # stores local file on server
    ftp.quit()
