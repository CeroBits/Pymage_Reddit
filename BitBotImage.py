import praw
import urllib.request
import time
import re
import socket
import os

socket.getaddrinfo('localhost', 8080)

print("Connecting...")
reddit = praw.Reddit('Tracker')
print("Success, retrieving threads.")
subRedditName = "INSER_SUBREDDIT_NAME"
subreddit = reddit.subreddit(subRedditName)
contador =0
print("Leyendo archivo")
encontro=None

archivoName ="imagenesDescargadas.txt"
newpath = "C:\\Users\\garon\\Desktop\\ImagesBitBot\\"+subRedditName

if not os.path.exists(newpath):
    os.makedirs(newpath)
f=open("C:\\Users\\garon\\Desktop\\ImagesBitBot\\"+archivoName,"r")	
#for submission in subreddit.hot(limit=1000):
for submission in subreddit.top(limit=400):
	#print("Title: ", submission.title)
	#print("Text: ", submission.selftext) http://citaslegalizaciones.mppre.gob.ve/principal/inicio
	#print("Score: ", submission.score)
	#print("url: ", submission.url)
	#---------------------------------------------------------------------------------
	contador+=1
	postName = submission.title
	cleanedName = re.sub('[^a-zA-Z0-9-_*.]', '', postName)
	extension = submission.url[-4:len(submission.url)] 
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', '/u/BitBotDownload: this is a prototype of scraper, still learning')]
	urllib.request.install_opener(opener)		
	if extension ==".jpg" or extension ==".png" or extension ==".gif":			
		f=open("C:\\Users\\garon\\Desktop\\ImagesBitBot\\imagenesDescargadas.txt","r")	
		archivo= f.readlines()		
		for linea in archivo:
			if linea.strip('\r\n') == cleanedName:				
					encontro=True
					break												
			else:	
					encontro=False		
		print("---------------------------------\n")
		if encontro!=True:
			f=open("C:\\Users\\garon\\Desktop\\ImagesBitBot\\imagenesDescargadas.txt","a")
			f.write("\n"+cleanedName)
			urllib.request.urlretrieve(submission.url,"C:\\Users\\garon\\Desktop\\ImagesBitBot\\"+subRedditName+"\\"+cleanedName+extension)	
			print("Guardando: "+cleanedName+extension)
			f.close()
		else: 
			print("Se encontro NO se guarda: "+cleanedName+extension)				
			f.close()
		print("---------------------------------\n")
	#time.sleep(2)