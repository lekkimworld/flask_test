# Python Flask Example
Example of a Python flask app with gunicorn as the WSGI (web server gateway interface).

## Run directly
1. Create a virtual environment `python3 -m venv env`
2. Activate the virtual environment `source env/bin/activate`
3. Install dependencies `pip3 install -r requirements.txt`
4. Run `gunicorn wsgi:app`

## Build docker
1. Build `docker build --tag lekkim-python-server .`
2. Run `docker run --rm -p 8080:8080 lekkim-python-server`

