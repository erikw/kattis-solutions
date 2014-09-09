#!/usr/bin/env bash
printf "%s\t\t\t\t\t\t\t\t%s\n" "actual" "expected"
for i in {0..7}; do
	./listgame2.py < in$i | diff -y - out$i
done
