#!/usr/bin/bash

INC=0
NUM=1


if [ -n "$1" ]; then 
    NUM="$1"
fi

echo "Creating $NUM UUID..."
source venv/scripts/activate

while [ $INC -lt $NUM ]; do
    python main.py
    ((INC++))
done

deactivate

exec "$@"