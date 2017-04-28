#!/bin/bash

cd /opt/ctf/sample_py/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/sample_py 2>/dev/null
else
  qemu-x86_64 ../ro/sample_py 2>/dev/null
fi