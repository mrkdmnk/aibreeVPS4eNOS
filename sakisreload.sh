#!/bin/bash
sudo sakis3g disconnect
sudo systemctl stop openvpn
sudo sakis3g connect -console -cleanscrean -s -g MENU=CONNECT OTHER="USBMODEM" USBMODEM="12d1:155e" USBINTERFACE="0" APN="Internet" APN_USER="" APN_PASS=""
sudo systemctl start openvpn
