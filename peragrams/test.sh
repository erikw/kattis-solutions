#!/usr/bin/env bash
for i in {0..7}; do
	cat $i; ./peragram.py < $i
	echo "=======";
done
