FROM ubuntu:16.04
WORKDIR /opt
COPY requirements.txt /opt/
RUN apt-get update && apt-get install -y python python-pip && pip install -r requirements.txt
COPY app.py /opt/
COPY templates /opt/
COPY static /opt/
ENTRYPOINT ["python", "/opt/app.py"]
