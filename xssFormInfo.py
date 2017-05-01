import os
from bs4 import BeautifulSoup
import urllib2

input_variables={}
#Read HTML File from current folder.
for root,dir,files in os.walk("/home"):

    for file in files:
        if file.endswith(".php") or file.endswith(".html"):
            #print "found HTML file : " + file

            if(file == 'testPhp.php' or file == 'test1.html' ):
                input_variables[file] = []
                page =open(os.path.join(root,file))
                soup = BeautifulSoup(page.read())
                inputs = soup.find_all("input")
                for input in inputs:
                    try:
                        if input['name']:
                            input_variables[file].append(input['name'])
                    except:
                        continue
print input_variables
