import sys,os
from shutil import copyfile

directory = sys.argv[1]
cwrapperfile = '/home/team9/code/csanitizer_wrapper.c'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith("_c")]:
		newname = "old_" + filename
		newpath = os.path.join(dirpath, newname)
		oldpath = os.path.join(dirpath, filename)
		oldpathdotc = oldpath + '.c'
		
		os.rename(oldpath, newpath)
		
		with open(cwrapperfile, 'r') as infile, open(oldpathdotc, 'w') as outfile:
			for line in infile:
				line = line.replace('{0}', newpath)
				outfile.write(line)
		
		cmd = 'gcc ' + oldpathdotc + ' -o ' + oldpath
		os.system(cmd)
