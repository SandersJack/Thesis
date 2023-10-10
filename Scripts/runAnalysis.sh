#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

echo "Running Script!"
source $parent_path/.venv/Scripts/activate
python $parent_path/PDF2txt.py
python $parent_path/wordCount.py
