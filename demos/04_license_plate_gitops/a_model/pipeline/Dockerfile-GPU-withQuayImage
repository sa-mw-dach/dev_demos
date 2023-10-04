FROM quay.io/manhah/license_plate_demo_gpu_air-gapped:latest as build
WORKDIR /opt/app-root/src

# Activate venv so that future CMD and RUN commands in this Dockerfile 
# are automatically executed in this venv.
ENV VIRTUAL_ENV=/tmp/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY external/licence-plate-workshop/ .
ENV FLASK_APP=wsgi.py 
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000/tcp
