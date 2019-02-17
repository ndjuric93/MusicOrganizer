#!/bin/sh

export PYTHONPATH=$(pwd):${PYTHONPATH}
python micro_gateway/app.py
