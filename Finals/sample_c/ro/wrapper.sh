#!/bin/bash

cd /opt/ctf/sample_c/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/sample_c 2>/dev/null
else
  qemu-x86_64 ../ro/sample_c 2>/dev/null
fi