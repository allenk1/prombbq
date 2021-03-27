FROM python:3

# Install software for bluepy
RUN apk add --update alpine-sdk glib-dev

WORKDIR /usr/src/prombbq

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

CMD [ "python", "./monitor.py"]