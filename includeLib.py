import sys

filename = sys.argv[1]
executeCommands=['system','exec']
flag=0
startline="main("
brace="{"
check1="\nargv = init(argc, argv);\nif (checkShellCode(argc,argv)!=0 || checkPathVulnerability(arc,argv)!=0){\nreturn 1;\n}\n"
check2="\nargv = init(argc, argv);\nif (checkShellCode(argc,argv)!=0 || checkPathVulnerability(arc,argv)!=0 || checkCommandInjection(argc,argv)!=0){\nreturn 1;\n}\n"
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
