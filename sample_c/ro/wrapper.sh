#/bin/bash

cd /opt/ctf/sample_c/rw

if [[ "i386" == "i386" ]] || [[ "x86_64" == "i386" ]] ; then
  ../ro/sample_c 2>/dev/null
else
  qemu-i386 ../ro/sample_c 2>/dev/null
fi
