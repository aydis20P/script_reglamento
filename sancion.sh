#!/bin/bash

clear
shuf -n 1 sanciones_sueltas.json \
  | python -m json.tool
