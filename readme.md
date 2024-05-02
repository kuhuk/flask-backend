Command to update requirements.txt:     pip3 freeze > requirements.txt

To run command flask run:
Command to add FLASK_APP env variable:  export FLASK_APP=server.py
Command to add FLASK_ENV env variable:  export FLASK_ENV=development

Database commands:
export DB_USERNAME="kuhukcodes"
export DB_PASSWORD="yolo123"
python3 init_db.py

psql commands:
To enter psql, run command:     psql postgres
Command to start connection with the database:      \c <dn_name> [example: \c portfolio]
To switch user after connecting with a database, use command:       \c - <username> [example: \c - kuhukcodes]
To see login info inside a DB, use command:     \conninfo
To see contents of a table, run command:    SELECT name, email, message FROM messages;

Python virtual environment commands:
1. Command to create virtual environment:    python3 -m venv .venv
2. Command to start virtual environment:     source .venv/bin/activate