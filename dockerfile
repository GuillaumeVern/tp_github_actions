ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base
COPY ./boa.py .
CMD python -m unittest boa.py