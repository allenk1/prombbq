FROM arm32v7/python:3

# Install software for bluepy
RUN apt-get install libglib2.0-dev

WORKDIR /usr/src/prombbq

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

CMD [ "python", "./monitor.py"]