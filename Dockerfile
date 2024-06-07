FROM python:3.10-slim
WORKDIR /code/
COPY ./src/ /code/src/

CMD python3 src/main.py
