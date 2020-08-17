from ftplib import FTP
import time
import os

host = "speedtest.tele2.net"

def timer_dec(func):
	def dec(*args,**kwargs):
		start_time = time.time()
		func(*args,**kwargs)
		print("--- %s total seconds ---" % (time.time() - start_time))    
	return dec

ftp = FTP(host=host)
ftp.login("", "")

@timer_dec
def _file(filename):
	with open(filename, "wb+") as file:
		ftp.retrbinary(f"RETR {filename}", file.write)
		ftp.storbinary(f'STOR /upload/{filename}', file)
	os.remove(filename)



_file('1KB.zip')
_file('1MB.zip')
_file('2MB.zip')
_file('3MB.zip')
ftp.quit()