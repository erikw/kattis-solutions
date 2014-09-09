#!/usr/bin/env bash

for i in {1000..10000}; do
    echo "$i"  | ./listgame2.py
    if [[ "$?" != "0" ]]; then
	exit $?
    fi
done
