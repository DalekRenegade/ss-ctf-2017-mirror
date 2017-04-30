""" 
command to use it is:
python directory_searcher.py <file_path>
Version 1: You will get an output of all the environment variables being accessed by the 
os.environ command and the line number it exists on in the particular file.

"""
import os
import glob
from sys import argv
import re


os.chdir(argv[1])
for file in glob.glob("*.py"):
	with open(file, 'r') as f1:
		lines = f1.readlines()
		for lineNum, line in enumerate(lines):
						
			if 'os.environ' in line:
				m=re.search(r"\[\'([A-Za-z0-9_]+)\'\]",line)
				if m:
					print("\t\t\t ----Information for attacking---- ")
					print m.group(1)+'\tLine Number: '+str(lineNum)+"\tin file: "+str(file)					
					lines[lineNum]=lines[lineNum].replace(m.group(1),str(os.getenv(m.group(1))))
		
	with open(file, 'w') as f1:
		f1.writelines(lines)
	

"""	fp = open(file, "r")
	for lineNum, line in enumerate(fp.readlines(),1):
		if 'os.system' in line:
			#print file
			pass
		if 'os.environ' in line:
			#print file
			m = re.search(r"\[\'([A-Za-z0-9_]+)\'\]",line)
			if m:
				print m.group(1)+'\tLine Number: '+str(lineNum)+"\tin file: "+str(file)

			fp.close()
"""
