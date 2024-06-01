#!/bin/sh

# Initialize the database
python init_db.py

# Start the Flask app
exec python app.py

