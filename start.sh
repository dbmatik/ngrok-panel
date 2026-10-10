#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
xdg-open http://127.0.0.1:5000 || open http://127.0.0.1:5000 || start http://127.0.0.1:5000
python3 app.py
