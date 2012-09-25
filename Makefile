PYTHON = python

.PHONY: build force clean distclean

.DEFAULT: build

build:
	$(PYTHON) setup.py build_ext --inplace

force:
	$(PYTHON) setup.py build_ext --inplace -f

install:
	python setup.py install

clean:
	-rm -rf build
	-rm src/p2t.cpp
	-rm p2t.so

distclean: clean
	-git clean -dxf
