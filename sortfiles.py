from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import sys
import os
import json
import time
import fnmatch
from pathlib import Path
import shutil

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" + filename
			new_destination = folder_destination + "/" + filename
			os.rename(src, new_destination)

def FixSameName(direct, fileName):
	
	tempfilename = str(round(((time.time()*400-1620300000*400))/20000))+fileName
	os.rename(direct+fileName, direct+tempfilename)
	return tempfilename

def NormalSort():
	folder_to_track = sys.argv[1]
	
	for file_name in os.listdir(folder_to_track):
		if fnmatch.fnmatch(file_name, '*.txt') or fnmatch.fnmatch(file_name, '*.doc') or fnmatch.fnmatch(file_name, '*.html') or fnmatch.fnmatch(file_name, '*.pdf'):
			d = Path(folder_to_track+'Documents')
			d.mkdir(exist_ok=True)
			print("Document: " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Documents/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Documents/')
			
		elif fnmatch.fnmatch(file_name, '*.jpg') or fnmatch.fnmatch(file_name, '*.JPG') or fnmatch.fnmatch(file_name, '*.jpeg') or fnmatch.fnmatch(file_name, '*.png') or fnmatch.fnmatch(file_name, '*.bmp') or fnmatch.fnmatch(file_name, '*.kra'):
			p = Path(folder_to_track+'Photos')
			p.mkdir(exist_ok=True)
			print("Photo:    " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Photos/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Photos/')
			
		elif fnmatch.fnmatch(file_name, '*.xlr') or fnmatch.fnmatch(file_name, '*.xls') or fnmatch.fnmatch(file_name, '*.xlsx') or fnmatch.fnmatch(file_name, '*.xps'):
			s = Path(folder_to_track+'Sheets')
			s.mkdir(exist_ok=True)
			print("Sheet:    " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Sheets/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Sheets/')
			
		elif fnmatch.fnmatch(file_name, '*.mp3') or fnmatch.fnmatch(file_name, '*.wav'):
			a = Path(folder_to_track+'Audio')
			a.mkdir(exist_ok=True)
			print("Audio:    " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Audio/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Audio/')
			
		elif fnmatch.fnmatch(file_name, '*.mp4') or fnmatch.fnmatch(file_name, '*.avi') or fnmatch.fnmatch(file_name, '*.AVI'):
			v = Path(folder_to_track+'Video')
			v.mkdir(exist_ok=True)
			print("Video:    " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Video/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Video/')
			
		elif fnmatch.fnmatch(file_name, '*.exe') or fnmatch.fnmatch(file_name, '*.apk'):
			e = Path(folder_to_track+'Executables')
			e.mkdir(exist_ok=True)
			print("Exec:     " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Executables/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Executables/')
			
		elif os.path.isdir(os.path.join(folder_to_track, file_name)) != True:
			m = Path(folder_to_track+'Miscellaneous')
			m.mkdir(exist_ok=True)
			print("Misc:     " + file_name)
			try:
				shutil.move(folder_to_track+file_name, folder_to_track+'/Miscellaneous/')
			except:
				shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Miscellaneous/')
				
def RecursiveSort():
	folder_to_track = sys.argv[2]
	
	directoryList = []
	directoryList.append(folder_to_track)
	for file_name in os.listdir(folder_to_track):
		if os.path.isdir(os.path.join(folder_to_track, file_name)):
			if file_name != "Documents" and file_name != "Photos" and file_name != "Sheets" and file_name != "Audio" and file_name != "Video" and file_name != "Executables" and file_name != "Miscellaneous":
				directoryList.append(os.path.join(folder_to_track, file_name) + "/")
				#print(os.path.join(folder_to_track, file_name) + "/")
			
	for directory in directoryList:
				
		for file_name in os.listdir(directory):
		
			if os.path.isdir(os.path.join(directory, file_name)):
				if file_name != "Documents" and file_name != "Photos" and file_name != "Sheets" and file_name != "Audio" and file_name != "Video" and file_name != "Executables" and file_name != "Miscellaneous":
					if os.path.join(directory, file_name) + "/" not in directoryList:
						directoryList.append(os.path.join(directory, file_name) + "/")
				
			elif fnmatch.fnmatch(file_name, '*.txt') or fnmatch.fnmatch(file_name, '*.doc') or fnmatch.fnmatch(file_name, '*.html') or fnmatch.fnmatch(file_name, '*.pdf'):
				d = Path(folder_to_track+'Documents')
				d.mkdir(exist_ok=True)
				print("Document: " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Documents/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Documents/')
				
			elif fnmatch.fnmatch(file_name, '*.jpg') or fnmatch.fnmatch(file_name, '*.JPG') or fnmatch.fnmatch(file_name, '*.jpeg') or fnmatch.fnmatch(file_name, '*.png') or fnmatch.fnmatch(file_name, '*.bmp') or fnmatch.fnmatch(file_name, '*.kra'):
				p = Path(folder_to_track+'Photos')
				p.mkdir(exist_ok=True)
				print("Photo:    " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Photos/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Photos/')
				
			elif fnmatch.fnmatch(file_name, '*.xlr') or fnmatch.fnmatch(file_name, '*.xls') or fnmatch.fnmatch(file_name, '*.xlsx') or fnmatch.fnmatch(file_name, '*.xps'):
				s = Path(folder_to_track+'Sheets')
				s.mkdir(exist_ok=True)
				print("Sheet:    " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Sheets/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Sheets/')
				
			elif fnmatch.fnmatch(file_name, '*.mp3') or fnmatch.fnmatch(file_name, '*.wav'):
				a = Path(folder_to_track+'Audio')
				a.mkdir(exist_ok=True)
				print("Audio:    " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Audio/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Audio/')
				
			elif fnmatch.fnmatch(file_name, '*.mp4') or fnmatch.fnmatch(file_name, '*.avi') or fnmatch.fnmatch(file_name, '*.AVI'):
				v = Path(folder_to_track+'Video')
				v.mkdir(exist_ok=True)
				print("Video:    " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Video/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Video/')
				
			elif fnmatch.fnmatch(file_name, '*.exe') or fnmatch.fnmatch(file_name, '*.apk'):
				e = Path(folder_to_track+'Executables')
				e.mkdir(exist_ok=True)
				print("Exec:     " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Executables/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Executables/')
				
			elif os.path.isdir(os.path.join(directory, file_name)) != True:
				m = Path(folder_to_track+'Miscellaneous')
				m.mkdir(exist_ok=True)
				print("Misc:     " + file_name)
				try:
					shutil.move(directory+file_name, folder_to_track+'/Miscellaneous/')
				except:
					shutil.move(directory+FixSameName(directory, file_name), folder_to_track+'/Miscellaneous/')
	count = int(0)
	while count < len(directoryList):
		if directoryList[len(directoryList) - 1 - count] != folder_to_track:
			print("Dir:      " + directoryList[len(directoryList) - 1 - count])
			os.rmdir(directoryList[len(directoryList) - 1 - count])
		count += 1
	
def HelpMenu():
	print("Normal syntax: sort -[action] [destination]\n")
	print("Actions:")
	print("-r	Recursive, looks in all folders. BE CAREFUL, this can break programs and such that use relative files.")
	
	
if len(sys.argv) > 1:
	if sys.argv[1].upper() == "-HELP":
		HelpMenu()
	elif sys.argv[1].upper() == "-R":
		if len(sys.argv) > 2:
			RecursiveSort()
		else:
			sys.argv.append(os.getcwd() + "/")
			RecursiveSort()
	else:
		try:
			if os.listdir(sys.argv[1]):
				NormalSort()
		except:
			print("sort /example/example/")
			print("             ↑")
			print("Error, please specify file path.\n")
else:
	print("sort argument here")
	print("     ↑")
	print("Syntax error, expected argument.\n")
	print("If you need assistance, type 'sort -help' to show the help menu.\n")


