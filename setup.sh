#!/usr/bin/env sh

mkdir "$1"
cat > "$1/$1.py" << ENDOFSTRING
#!/usr/bin/env python

import sys

def main():
    return 0

if __name__ == '__main__':
	sys.exit(main())
ENDOFSTRING

chmod u+x "$1/$1.py"

# Fetch sample files.
wget --quiet -O "$1/samples.zip" "https://open.kattis.com/problems/$1/file/statement/samples.zip"
unzip -q "$1/samples.zip" -d "$1"
rm "$1/samples.zip"

# Hack to rename files if there is only one sample input.
if [ -f "$1/sample.in" ]; then
	mv "$1/sample.in" "$1/0.in"
fi
if [ -f "$1/sample.ans" ]; then
	mv "$1/sample.ans" "$1/0.ans"
fi
