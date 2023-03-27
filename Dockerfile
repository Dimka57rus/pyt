# Download ubuntu from docker hub
FROM ubuntu:20.04

# Download updates and install python3, pip and vim
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y

COPY src src
RUN pip install -r src/requirements.txt
CMD ["python3", "./src/bot_v2.py"]
