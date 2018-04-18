#!/bin/sh
rm -rf ./environment-flisol
echo 'installing flisol requirements'
echo 'type sudo password'
sudo pip install virtualenv
virtualenv -p /usr/bin/python2.7 ./environment-flisol
source ./environment-flisol/bin/activate
pip install -r requirements.txt
out=$(python 1_opencv_python_samples/0_opencv_version.py)

compare_version="3.4.0"
if [ "$out" == "$compare_version" ] 
then
	clear
	echo 'install ok'
else
	echo "error on installation"
fi
deactivate
