.PHONY: install
install:
	poetry install

.PHONY: run
run:
	poetry run python reverse-ip.py

