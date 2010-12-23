#!/bin/bash

mkdir /tmp/ramdisk; chmod 777 /tmp/ramdisk
mount -t tmpfs -o size=32M tmpfs /tmp/ramdisk/
cp budget.db /tmp/ramdisk
chmod 666 /tmp/ramdisk/budget.db
