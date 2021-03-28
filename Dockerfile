FROM arm32v7/python:3-slim

WORKDIR /usr/src/prombbq

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

CMD [ "python", "./monitor.py"]