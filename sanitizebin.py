import sys,os

directory = sys.argv[1]
files=[]
D={}
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in [f for f in filenames if f.endswith(".c")]:
        files.append(os.path.join(dirpath, filename))
envVar=os.system("printenv>environment1.txt")
with open("environment.txt", 'r') as f1:
			lines = f1.readlines()
for x in lines:
	y=x.index("=")
	D[x[:y]]=x[y+1:].strip("\n")
i=0
lines=[]
for filename in files:
	with open('test.c', 'r') as f1:	
		lines = f1.readlines()
		for i in range(0,len(lines)):
			for key in D:
				str1="secure_getenv(\""+key+"\")"
				str2="getenv(\""+key+"\")"
				if str1 in lines[i]:
					value="\""+D[key]+"\""
					lines[i]=lines[i].replace(str1,value)
				if str2 in lines[i]:
					value="\""+D[key]+"\""
					lines[i]=lines[i].replace(str2,value)
	with open('test.c', 'w') as f1:	
		f1.writelines(lines)
