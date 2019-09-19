#!/bin/bash
if [ dpkg -s python3-pip -ne 0 ];then
    sudo apt install python3-pip
else 
    echo Python3-pip installed already
fi
sudo pip3 install --upgrade pip
if [ 'pip3 list | grep django' ];then
    echo Django installed already.
else
    echo Installing Django ...
    sudo pip3 install django
fi
if [ 'pip3 list | grep django-cors-headers' ];then
    echo django-cors-headers installed already.
else
    echo Installing django-cors-headers ...
    sudo pip3 install django-cors-headers
fi
if [ 'pip3 list | grep djangorestframework' ];then
    echo djangorestframework installed already.
else
    echo Installing djangorestframework ...
    sudo pip3 install djangorestframework
fi
if [ 'pip3 list | grep paramiko' ];then
    echo paramiko installed already.
else
    echo Installing paramiko ...
    sudo pip3 install paramiko
fi
if [ 'pip3 list | grep xlrd' ];then
    echo xlrd installed already.
else
    echo Installing xlrd ...
    sudo pip3 install xlrd
fi
if [ 'pip3 list | grep pandas' ];then
    echo pandas installed already.
else
    echo Installing pandas ...
    sudo pip3 install pandas
fi
if [ 'pip3 list | grep django-bootstrap3' ];then
    echo django-bootstrap3 installed already.
else
    echo Installing django-bootstrap3 ...
    sudo pip3 install django-bootstrap3
fi
if [ 'pip3 list | grep pandas' ];then
    echo social-auth-app-django installed already.
else
    echo Installing social-auth-app-django ...
    sudo pip3 install social-auth-app-django
fi
if [ 'pip3 list | grep mysqlclient' ];then
    echo mysqlclient installed already.
else
    echo Installing mysqlclient ...
    sudo pip3 install mysqlclient
fi
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev

