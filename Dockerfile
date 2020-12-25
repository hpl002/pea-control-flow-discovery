FROM python:3.9.1

RUN apt-get update
RUN apt-get install graphviz gcc libgraphviz-dev -y 


COPY ./app/ /app
WORKDIR /app 
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]

EXPOSE 8080

# Label docker image
LABEL app=pea:control-flow-discovery