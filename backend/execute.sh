#!/bin/bash


kill -9 $(lsof -t -i:5000)

python3 app.py