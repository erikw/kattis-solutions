#!/usr/bin/env sh

mkdir "$1"
cat > "$1/$1.py" << ENDOFSTRING
#!/usr/bin/env python 

def main():
    pass

if __name__ == '__main__':
    main()
ENDOFSTRING

