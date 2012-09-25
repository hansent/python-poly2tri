PYTHON = python

.PHONY: build force clean distclean

build:
	$(PYTHON) setup.py build_ext --inplace

force:
	$(PYTHON) setup.py build_ext --inplace -f

install:
	python setup.py install

clean:
	-rm -rf build
	-find p2t.so
	-find . -iname '*.pyc' -exec rm {} \;
	-find . -iname '*.pyo' -exec rm {} \;

distclean: clean
	-git clean -dxf


