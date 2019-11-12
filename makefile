all: run

run: primer.x primer.cpp
	./primer.x

primer.x: primer.cpp
	g++ primer.cpp -o primer.x

clean:
	rm primer.x

.PHONY: all run
