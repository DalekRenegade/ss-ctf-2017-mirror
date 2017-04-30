import sys,os

directory = sys.argv[1]
files=[]
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".c")]:
        files.append(os.path.join(dirpath, filename))
        
executeCommands=['system','exec']
flag=0
startline="main("
brace="{"
check1="\nargv = init(argc, argv);\n"
check2="\nargv = init2(argc, argv);\n"
for filename in files:
	with open(filename, 'r') as f1:
		lines = f1.readlines()

	lines[1]=lines[1]+ "#include<cpatcher.h>\n#include<cpatchersys.h>\n"
	for i in range(0,len(lines)):
		if executeCommands[0] in lines[i]:
			flag =1
			break
		if executeCommands[1] in lines[i]:
			flag =1
			break

	for i in range(0,len(lines)):
		if startline in lines[i]:
			if flag == 1:
				if brace in lines[i]:
					lines[i]=lines[i]+check2
				elif brace in lines[i+1]:
					lines[i+1]=lines[i+1]+check2
				break
			else:
				if brace in lines[i]:
					lines[i]=lines[i]+check1
				elif brace in lines[i+1]:
					lines[i+1]=lines[i+1]+check1
				break

	with open(filename, 'w') as f2:
		f2.writelines(lines)
