FROM registry.access.redhat.com/ubi8/python-38 as build
WORKDIR /opt/app-root/src
RUN python3 -m venv /tmp/.venv && . /tmp/.venv/bin/activate
RUN python -m pip install --upgrade pip
COPY external/licence-plate-workshop/ .
RUN pip install -r requirements.txt
ENV FLASK_APP=wsgi.py 
CMD ["flask", "run"]
EXPOSE 5000/tcp
