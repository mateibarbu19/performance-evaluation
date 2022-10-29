#!/bin/bash

# Tell bash to exit after SIGINT
trap "exit" INT

# Write a 100MB file every loop
while true; do
    dd if=/dev/zero of=100MBfile bs=512 count=200000 oflag=dsync &> /dev/null
done
