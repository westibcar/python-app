FROM python:3.12.10-alpine
LABEL maintainer="@udayacademy"

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

CMD python /src/app.py
