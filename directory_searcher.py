import os
import glob
from sys import argv
import re


os.chdir(argv[1])
for file in glob.glob("*.py"):
	fp = open(file, "r")
	for lineNum, line in enumerate(fp.readlines(),1):
		if 'os.system' in line:
			#print file
			pass
		if 'os.environ' in line:
			#print file
			m = re.search(r"\[\'([A-Za-z0-9_]+)\'\]",line)
			if m:
				print m.group(1)+'\tLine Number: '+str(lineNum)

			fp.close()

