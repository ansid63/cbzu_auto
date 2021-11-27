FROM python:3.8.12


WORKDIR ${WDIR}

RUN apk update && apk upgrade

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

