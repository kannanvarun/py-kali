ifneq ($(OS), WINDOWS_NT)
run:
	python3 my-package/main.py

install:
	pip3 install -r requirements.txt

build:
	python3 -m build

clean:
	rm -rf build
	rm -rf dist
	rm -rf my_package.egg-info
endif
