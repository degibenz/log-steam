
pylint:
	python3 -m pylint src/

pytest:
	python3 -m pytest src/

pyenv:
	pip3 install pipenv==2018.11.26 && pip install --upgrade pip && pipenv install --deploy --system --clear

build:
	docker build -t log-server:latest .