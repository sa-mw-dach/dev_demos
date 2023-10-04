FROM quay.io/manhah/license_plate_demo_gpu_air-gapped:latest as build
WORKDIR /opt/app-root/src
RUN python3 -m venv /tmp/.venv && . /tmp/.venv/bin/activate
COPY external/licence-plate-workshop/ .
ENV FLASK_APP=wsgi.py 
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000/tcp
