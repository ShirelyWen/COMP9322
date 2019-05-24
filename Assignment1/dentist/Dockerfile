FROM alpine:latest
RUN apk add --no-cache python3-dev 
RUN pip3 install --upgrade pip 
WORKDIR /service
COPY ./app /service
RUN pip3 install -r requirements.txt 
RUN pip3 install swagger_py_codegen
EXPOSE 5000
CMD python3 demo/__init__.py
