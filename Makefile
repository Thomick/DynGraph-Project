.PHONY: all
all:
	python3 main.py

.PHONY: clean
clean:
	rm -v data/*_*
