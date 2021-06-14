# Pull base image
FROM resin/rpi-raspbian:jessie
# Comment out the above line and use the following for intel based machines
# FROM debian:bullseye

# Install dependencies
RUN apt-get update && apt-get install -y \
    vim \
    python3 \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    python3-wheel \
    gcc \
    build-essential \
    libglib2.0-dev \
    bluez \
    libbluetooth-dev \
    libboost-python-dev \
    git \ 
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/prombbq

COPY . ./
RUN pip3 install -r requirements.txt

# fix library problem for python3 & libboost
RUN mv /usr/lib/arm-linux-gnueabihf/libboost_python-py27.so.1.55.0 /usr/lib/arm-linux-gnueabihf/libboost_python-py27.so.1.55.0-old
RUN ln -s /usr/lib/arm-linux-gnueabihf/libboost_python-py34.so.1.55.0 /usr/lib/arm-linux-gnueabihf/libboost_python-py27.so.1.55.0

CMD [ "python3", "./monitor.py"]