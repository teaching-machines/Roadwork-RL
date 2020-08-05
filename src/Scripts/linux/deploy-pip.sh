#!/bin/bash
if [ -z $1 ]; then
  echo "Usage: $0 <PACKAGE_DIRECTORY>"
  echo "Example: $0 $(pwd)/Lib/python/roadwork"
  exit 1
fi

PACKAGE_PATH=$1
CURRENT_PATH=$(pwd)

cd $PACKAGE_PATH

echo "Removing old builds"
sudo rm -rf $PACKAGE_PATH/dist/

echo "Creating package"
sudo python3 $PACKAGE_PATH/setup.py sdist
pip install twine

echo "Uploading to PyPi"
twine upload $PACKAGE_PATH/dist/*

# cd $CURRENT_PATH
