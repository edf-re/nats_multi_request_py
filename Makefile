setup:
	pipenv install

test-unit:
	echo TODO
	exit 1

build-docs:
	cd docs
	pipenv run make html
	
release:
	rm -rf dist
	python3 -m build
	twine upload dist/*
	git tag -a v`cat version`
