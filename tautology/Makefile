name=all.py
pyfile= $(filter-out $(name), $(wildcard *.py))

$(name): $(pyfile)
	cat $^ | grep -ve "^\s*\(from\|#!\/\)" | sed -e '/^\s*$$/d' > $@

clean:
	$(RM) $(name)
