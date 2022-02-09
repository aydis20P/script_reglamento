#!/bin/bash

clear
shuf -n 1 textos_sueltos.json \
  | python -m json.tool
