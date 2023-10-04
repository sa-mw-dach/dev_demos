FROM registry.access.redhat.com/ubi8/python-38 as build

# Install dependencies
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Set working directory and copy files from git repo
WORKDIR /opt/app-root/src
COPY external/licence-plate-workshop/ .

# Launch Flask and expose port 5000
ENV FLASK_APP=wsgi.py 
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000/tcp
