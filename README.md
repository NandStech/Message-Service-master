# sendsmsbackend

A service that helps send message on behalf of any service that connects to it.

This service uses Twillo service foe its messaging. It also consists of two workers that at intervals check its database for new messages that entered into it. Ome caters for sending message while the other checks for any message that wasnt't sent initially.

## Note Before Building Images OR Runing Locally
- In both .env file replace <AUTH_TOKEN> with an actual Authentication Token from Twillo , along with with an Account Sid
- Also remember to change the database password and name.
- Insert Actual Private and Public Key into both .env file


## To Run Locally 

set it up
------

Create a virtual environment and install the requirements

    $ python3 -m venv ./venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt


Get the local database ready

    $ python init_db.py

Start the development server

    $ FLASK_APP=wsgi.py flask run
    * Serving Flask app "wsgi.py"
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit

Check the service at http://127.0.0.1:5000/


Tests
------

Run the unit tests with, Typically this is required, but for this module it is not required.

    $ pytest


Dependencies
------

MessageBackend uses Flask as a web framework, Flask RESTplus for creating the interface, and SQLAlchemy to handle the database models. It uses a SQLlite database for local development. It uses Celery to handle Asynchronous Task, while Rabbit Mq is used as a message broker.

Background Processses 
------

Ensure that the message broker Rabbit MQ is running in the background,if its not

    * Start the Rabbit MQ service
 
Start a Celery process in the bacground by running

    * celery worker -A celery_worker.celery --loglevel=info

start a celery beat in the background also

    *celery beat -A celery_worker.celery --loglevel=info

