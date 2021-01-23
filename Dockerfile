FROM python:3.9.1-slim

RUN apt-get update
RUN apt-get install graphviz gcc libgraphviz-dev -y 

COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app/ /app

WORKDIR /app 

RUN mkdir export
RUN mkdir upload

ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]

EXPOSE 8080

# Label docker image
LABEL app=pea:control-flow-discovery