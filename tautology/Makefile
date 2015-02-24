name=all.py
pyfiles= $(filter-out $(name), $(wildcard *.py))

.PHONY: clean

all: $(name)

$(name): $(pyfiles)
	echo "#!/usr/bin/env python2" > $@
	cat $^ | grep -ve "^\s*\(from\|#!\/\)" | sed -e '/^\s*$$/d' >> $@
	chmod 744 $@

clean:
	$(RM) $(name)
