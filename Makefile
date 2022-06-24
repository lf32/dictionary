PYTHON_EXE?=python
MANAGE=manage.py


run:
	${PYTHON_EXE} ${MANAGE} runserver 8001 --noreload --insecure

