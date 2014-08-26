#!/usr/bin/env bash
for i in {0..4}; do
	./queen < in$i | diff -y - out$i
done
