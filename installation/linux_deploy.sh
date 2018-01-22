#!/usr/bin/env bash

# Install python 3
echo Installing python version 3
sudo apt-get install python3

# Install pip
echo Installing pip version 3
sudo apt-get update
sudo apt install python3-pip

# Install Java
echo Installing Java jdk
sudo apt-get update
sudo apt-get install default-jr

# Install Git
echo Installing Git
sudo apt-get update
sudo apt-get install git

# Install Allure
echo Installing Allure report manager
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure

#Install umake
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make

# Install PyCharm
echo Installing PyCharm
umake ide pycharm

# Cloning project
echo Cloning gitlab project. Be ready to enter you LDAP credentials
cd ~/
mkdir PycharmProjects
cd PycharmProjects
git clone https://github.com/Goraved/testing_framework.git
cd ~/

# Running PyCharm
`find -name "pycharm.sh"`
xdg-open ~/PycharmProjects


echo Done <...> Done
echo Now you should open project from ~/PychramProjects using PyCharm

