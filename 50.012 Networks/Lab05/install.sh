#!/bin/bash
# Installation script for 50.012 Networks Lab 5
# Nils, SUTD, 2015

sudo apt-get install -y quagga curl screen python-setuptools
sudo easy_install termcolor

# soft-link the conf files to allow students to edit them directly
sudo ln -s conf/bgpd-R1.conf /etc/quagga/
sudo ln -s conf/bgpd-R2.conf /etc/quagga/
sudo ln -s conf/bgpd-R3.conf /etc/quagga/
sudo ln -s conf/bgpd-R4.conf /etc/quagga/
sudo ln -s conf/zebra-R1.conf /etc/quagga/
sudo ln -s conf/zebra-R2.conf /etc/quagga/
sudo ln -s conf/zebra-R3.conf /etc/quagga/
sudo ln -s conf/zebra-R4.conf /etc/quagga/
sudo chown quagga /etc/quagga/*.conf
