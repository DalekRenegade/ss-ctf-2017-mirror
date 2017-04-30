import re
import os
from sys import argv


def xss_check(match):
    match = match.group()
    # print "testInput(" + match + ")"
    return "testInput(" + match + ")"


html_purifier_header = "require_once '%s';\n header('X-XSS-Protection: 0');\n\n" % argv[1]

html_purifier_func = "function testInput($data){\n" \
	   "$purifier = new HTMLPurifier();\n" \
	   "$data1 = $purifier->purify($data);\n" \
       "$data1 = escapeshellcmd($data1);\n" \
	   "return $data1;\n" \
	"}"

directory = argv[2] if len(argv) > 2 else os.getcwd()

with open("input_vuls.txt", "a+") as log_file:

    for filename in os.listdir(directory):
        if filename.endswith(".php"):
            with open(directory + "/" + filename, 'r+') as f:

                lines = f.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if "$_GET" in line or "$_POST" in line or "$_COOKIE" in line:
                        # print line
                        log_file.write("%s --> %s" % (str(i), line))
                    line = re.sub(r'\$_GET\[.*?\]+', xss_check, line)
                    line = re.sub(r'\$_COOKIE\[.*?\]+', xss_check, line)
                    line = re.sub(r'\$_POST\[.*?\]+', xss_check, line)
                    lines[i] = line

                # print lines
                lines.insert(1, html_purifier_header)
                lines.insert(2, html_purifier_func)

                f.seek(0)
                f.writelines(lines)
                f.truncate()