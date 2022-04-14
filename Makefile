setup:
	pipenv install --skip-lock

release:
	rm -rf dist
	python3 -m build
	twine upload dist/*
	git tag -a v`cat VERSION`
