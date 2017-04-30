import os
import re

def findVariableValue(code,myQuery):
    for line in code:
        if myQuery in line and re.sub(myQuery+'[ =]', '', line):
            myQuery = line.split("=")[1].lstrip()
            return myQuery

def writeToFile(outputcode,code,fd):
    for line in code:
        if "mysql_query" in line and re.sub('mysql_query[ (]', '', line, re.IGNORECASE):
            for queryLine in outputcode:
                fd.write(queryLine)
        else:
            fd.write(line)


def cleanQuery(myQuery):
    #myQuery.index("$")
    indexes=[]
    for i,ch in enumerate(myQuery):
        if(ch=='$'):
            indexes.append(i)

    k = len(indexes)-1
    for i in range(0,len(indexes)):
            myQuery = myQuery[:indexes[k-i]] + "\\" + myQuery[indexes[k-i]:]

    return myQuery


def findQuery(line,code,filePath):
    parts = line.split("mysql_query")
    myQuery = parts[1].lstrip()
    myQuery =myQuery[myQuery.find("(")+1:myQuery.find(")")].lstrip()
    if(myQuery[0]=="$"):
        myQuery =myQuery.split(",")[0]
        myQuery = findVariableValue(code,myQuery).split(";")[0]
        myQuery=cleanQuery(myQuery)
    os.system("php -f ~/getReplaceStringSQL.php "+ myQuery +" > ~/outputfile.txt")
    found = False
    for root, dir, files in os.walk("/home"):
        for output in files:
            if output =="outputfile.txt":
                outputfile = open(os.path.join(root, output), 'r')
                outputcode = outputfile.readlines()
                fd = open(filePath, 'w')
                writeToFile(outputcode,code,fd)
                outputfile.close()
                os.system("rm ~/outputfile.txt")
                fd.close()
                found=True
                break
        if found:
            break



for root,dir,files in os.walk("/home"):
    for file in files:
        if file.endswith(".php") and file is not "getReplaceStringSQL.php":
            myFile=file
            file=open(os.path.join(root, file),'r')
            code =file.readlines()
            for  line in code:
                if "mysql_query" in line and re.sub('mysql_query[ (]','',line,re.IGNORECASE):
                    findQuery(line,code,os.path.join(root, myFile))
                    #print "Hi"
                    break
            file.close()



