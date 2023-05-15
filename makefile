default:
	@echo targets: venv install check test 

venv:
	@echo run: source ~/github/slexilAsModuleAndPackage/pySlexil/bin/activate

install:
	pip install . --upgrade

check:
	ls -lat ~/github/slexilAsModuleAndPackage/pySlexil/lib/python3.10/site-packages/slexil*
 
test:
	(cd tests; 	python -m unittest test_listTiers.py)
	(cd tests; 	python -m unittest test_morphemeGloss.py)
	(cd tests; 	python -m unittest test_infernoDemo.py)
	(cd tests; 	python -m unittest test_infernoDemo_toHTML.py)

