.PHONY: install
install:
	pip install -r requirements.txt
	pip install -r dev-requirements.txt

.PHONY: lint
lint:
	black app
	isort -rc -sl app
	autoflake --remove-all-unused-imports -i -r app
	isort -rc -m 3 app
	flake8 app
	mypy app

.PHONY: start
start:
	uvicorn app.main:app --reload
