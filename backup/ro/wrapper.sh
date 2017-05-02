#!/bin/bash

cd /opt/ctf/backup/rw

if [[ "i386" == "i386" ]] || [[ "x86_64" == "i386" ]] ; then
  ../ro/backup 2>/dev/null
else
  qemu-i386 ../ro/backup 2>/dev/null
fi