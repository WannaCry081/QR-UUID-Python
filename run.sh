#!/usr/bin/bash


ENV_PATH="$(pwd)/venv"
INC=0
NUM=1


if [ -d "$ENV_PATH" ]; then 
    echo "Activating virtual environment"
    source "$ENV_PATH/Scripts/activate"
else
    echo "Creating virtual environment"
    virtualenv "$ENV_PATH"
    source "$ENV_PATH/Scripts/activate"
    pip install -r "$(pwd)/requirements.txt"
fi


if [ -n "$1" ]; then 
    NUM="$1"
fi

echo "Creating $NUM UUID..."

while [ $INC -lt $NUM ]; do
    python main.py
    ((INC++))
done

deactivate


exec "$@"