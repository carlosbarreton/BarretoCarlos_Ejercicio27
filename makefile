all: run


run: primer.py primer.x primer.cpp
	./primer.x
	python primer.py

primer.x: primer.cpp
	g++ primer.cpp -o primer.x

clean:
	rm primer.x primerorden.png

.PHONY: all run
