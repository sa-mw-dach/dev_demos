cd /projects/dev_demos/
python3 -m venv /tmp/.venv && . /tmp/.venv/bin/activate
python -m pip install --upgrade pip
pip install -r external/licence-plate-workshop/requirements.txt
cd external/licence-plate-workshop/ 
FLASK_ENV=development FLASK_APP=wsgi.py flask run
