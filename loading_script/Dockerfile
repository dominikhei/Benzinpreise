FROM python:3

RUN pip install pandas datetime mysql-connector-python protobuf requests

ADD benzinpreise.py /

ADD benzinpreis_secrets.py /

CMD [ "python", "./benzinpreise.py" ]
