.PHONY: install
install:
	pip install -r requirements.txt
	pip install -r dev-requirements.txt

.PHONY: lint
lint:
	black app
	isort app/*.py
	flake8 app
	mypy app

.PHONY: start
start:
	uvicorn app.main:app --reload
