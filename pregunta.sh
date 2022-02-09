#!/bin/bash

clear
shuf -n 1 preguntas_sueltas.json \
  | python -m json.tool
