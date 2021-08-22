all:

clean:
	- rm *~ *.pyc
install:
	./setup.py build && sudo ./setup.py install
push:
	git push origin master

# git log -1 --format='%H' | cut -c 1-16
