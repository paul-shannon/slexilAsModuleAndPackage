default:
	@echo targets: venv install intall-via-setup check test 

venv:
	@echo run: source ~/github/slexilAsModuleAndPackage/pySlexil/bin/activate

install:
	pip install . --upgrade

install-via-setup:
	python setup.py install

twine:
	./pySlexil/bin/twine  upload --repository-url https://test.pypi.org/legacy/ dist/*

check:
	ls -lat ~/github/slexilAsModuleAndPackage/pySlexil/lib/python3.10/site-packages/slexil*
 
test:
	(cd tests; 	make test)
