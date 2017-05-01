ls /bin > /var/restricted_cmd.txt
chmod 444 /var/restricted_cmd.txt
cp /home/team9/code/csanitizer.h /usr/include/csanitizer.h
chmod 644 /usr/include/csanitizer.h
cp -a /opt/ctf/. /home/team9/ctf
