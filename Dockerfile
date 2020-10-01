FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python python-pip && pip install flask
COPY app.py /opt/
COPY templates /opt/
COPY static /opt/
ENTRYPOINT ["python", "/opt/app.py"]
