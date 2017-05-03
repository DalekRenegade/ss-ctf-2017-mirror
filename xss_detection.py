import re
import os
from sys import argv


def xss_check(match):
    match = match.group()
    # print "testInput(" + match + ")"
    return "testInput(" + match + ")"

purifier_path = "/root/htmlpurifier-4.9.2/library/HTMLPurifier.auto.php"

html_purifier_header = "\nrequire_once '%s';\n header('X-XSS-Protection: 0');\n\n" % purifier_path

html_purifier_func = "function testInput($data){\n" \
	   "$purifier = new HTMLPurifier();\n" \
	   "$data1 = $purifier->purify($data);\n" \
       "$data1 = escapeshellcmd($data1);\n" \
	   "return $data1;\n" \
	"}\n"

directory = argv[1] if len(argv) > 1 else os.getcwd()

with open("/var/log/xss-logs.log", "a+") as log_file:

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            #print os.path.join(subdir, file)
            filename = os.path.abspath(os.path.join(subdir, file))
            if filename.endswith(".php"):
                with open(filename, 'r+') as f:

                    lines = f.readlines()
                    start_tag_line = -1
                    for i in range(0, len(lines)):
                        line = lines[i]
                        if "<?php" in line and start_tag_line == -1:
                            start_tag_line = i
                        if "$_GET" in line or "$_POST" in line or "$_COOKIE" in line:
                            # print line
                            log_file.write("+%s %s \n %s" % (str(i+1), filename, line))
                        line = re.sub(r'\$_GET\[.*?\]+', xss_check, line)
                        line = re.sub(r'\$_COOKIE\[.*?\]+', xss_check, line)
                        line = re.sub(r'\$_POST\[.*?\]+', xss_check, line)
                        lines[i] = line

                    # print lines
                    lines.insert(start_tag_line+1, html_purifier_header + html_purifier_func)
                    # lines.insert(2, html_purifier_func)

                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
