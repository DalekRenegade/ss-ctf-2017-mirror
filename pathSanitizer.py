""" 
command to use it is:
python directory_searcher.py <starting_directory>
Version 1: Creates a file path-vulnerabilities.log which stores all the vulnerabilities in py and c files

"""
import os
import glob, sys
from sys import argv
import re

directory = sys.argv[1]
os.chdir(argv[1])
D={}
pythonLines=[] 
seaLions=[]
pythonFiles=[]
seaFiles=[]
with open("/tmp/path-vulnerabilities.log", "w") as create:
	create.write("Path Vulnerabilities\n")
fd = open("/tmp/path-vulnerabilities.log", "r+")
envVar=os.system("env| grep SESSION>/tmp/environment.txt")
with open("/tmp/environment.txt", 'r') as f1:
			envVarList = f1.readlines()
			print envVarList
for x in envVarList:
	y=x.index("=")
	D[x[:y]]=x[y+1:].strip("\n")
	print x[:y]
print ("Finding vulnerabilities in python")
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".py")]:
        pythonFiles.append(os.path.join(dirpath, filename))
  
for filecontent in pythonFiles:
	with open(filecontent, 'r') as f1:
		pythonLines = f1.readlines()
		for lineNum, line in enumerate(pythonLines):
						
			if 'os.environ' in line:
				m=re.search(r"\[\'([A-Za-z0-9_]+)\'\]",line)
				if m:
					towrite="vi +"+str(lineNum+1)+" "+ str(filecontent)+"\n"+ m.group(1)+"\n"
					fd.writelines(towrite)
					print towrite				
					pythonLines[lineNum]=pythonLines[lineNum].replace(m.group(1),str(os.getenv(m.group(1))))
		
	with open(filecontent, 'w') as f1:
		f1.writelines(pythonLines)
print ("Finding vulnerabilities in c")
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".c")]:
        seaFiles.append(os.path.join(dirpath, filename))
for filename in seaFiles:
	with open(filename, 'r') as fd1:	
		seaLions = fd1.readlines()
		for lineNum, line in enumerate(seaLions):
			for key in D:
				if key in line:
					str1="secure_getenv(\""+key+"\")"
					str2="getenv(\""+key+"\")"
					if str1 in seaLions[lineNum]:
						value="\""+D[key]+"\""
						seaLions[lineNum]=seaLions[lineNum].replace(str1,value)
					if str2 in seaLions[lineNum]:
						value="\""+D[key]+"\""
						seaLions[lineNum]=seaLions[lineNum].replace(str2,value)
					towrite="vi +"+str(lineNum+1)+" "+ str(filename)+"\nEnvironment variable used: "+ key+"\n"	
					fd.writelines(towrite)
					print towrite
			if "%n" in line:
				seaLions[lineNum]=seaLions[lineNum].replace("%n","%x")
				towrite="vi +"+str(lineNum+1)+" "+ str(filename)+"\n%n vulnerability"+"\n"	
				fd.writelines(towrite)
			if "%hhn" in line:
				seaLions[lineNum]=seaLions[lineNum].replace("%hhn","%x")
				towrite="vi +"+str(lineNum+1)+" "+ str(filename)+"\n%hhn vulnerability"+"\n"	
				fd.writelines(towrite)
			if ((not "printf\"" in line) and ("printf" in line)):
				towrite="vi +"+str(lineNum+1)+" "+ str(filename)+"\nprintf vulnerability"+"\n"	
				fd.writelines(towrite)
	with open(filename, 'w') as f2:	
		f2.writelines(seaLions)
					
fd.close()
