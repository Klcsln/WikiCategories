#!/bin/bash
pip install -r requirements.txt
docker pull mongo:4.2
docker run -d -p 27017:27017 --name categorydb mongo:4.2
python categoryParser.py $1