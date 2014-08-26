#!/usr/bin/env bash
printf "%s\t\t\t\t\t\t\t\t%s\n" "actual" "expected"
for i in {0..4}; do
	./queen < in$i | diff -y - out$i
done
