.PHONY: setup test run

run:
	.venv/bin/uvicorn app.main:app --reload-dir ./app --reload

setup:
	@python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements-dev.txt

test:
	.venv/bin/pytest
