if [ -z "$NBR" ]; then
	NBR=1
fi

clang++-3.6 -g -O2 -static -std=gnu++11 entertainmentbox.cc -o entertainmentbox && time ./entertainmentbox < $NBR.in | diff -y - $NBR.ans
