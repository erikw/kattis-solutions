name=all.py
pyfiles= $(filter-out $(name), $(wildcard *.py))

.PHONY: clean

$(name): $(pyfiles)
	cat $^ | grep -ve "^\s*\(from\|#!\/\)" | sed -e '/^\s*$$/d' > $@

clean:
	$(RM) $(name)
