ls /bin > /var/restricted_cmd.txt
chmod 444 /var/restricted_cmd.txt
cp ./cpatcher.h /usr/include/cpatcher.h
cp ./cpatchersys.h /usr/include/cpatchersys.h
chmod 644 /usr/include/cpatcher.h
chmod 644 /usr/include/cpatchersys.h
