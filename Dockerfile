FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# install app dependencies
RUN pip install flask
RUN pip install argparse

# Bundle app source
COPY simpleapp.py /src/simpleapp.py

EXPOSE 8000
CMD["python","/src/simpleapp.py","-p 8000"]
