#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | Default                           
# Settings and Default Variables of Framework, here you can
# change value of variables for adapter to your system.
#
# 
# Last Modified: 29/27/2016
#
#########################################################HEAD#


### SETTING FRAMEWORK ###

# Verbose Mode
"""Show all the alert messages."""
VERBOSE            =True

# Errors Log
"""Saves all error events in a log."""
ERROR_LOG          =True

# Apache Folder
"""Path of Apache2"""
PATCH_WWW          ="/var/www/html/"

# Enable Xterm
"""It shows processes that are running through wires, shown with xterm"""
XTERM_OPTION       =False

### END SETTING FRAMEWORK ###


# DEFAULT VARIABLES
"""Names of main files"""
KTFCONSOLE         ="ktf.console"
KTFLINKER          ="ktf.linker"
KTFRUN             ="ktf.run"
KTFLAB             ="ktf.lab"
KTFGUI             ="ktf.gui"
"""References"""
FOLDER_KATANA      ="/usr/share/KatanaFramework/"
KTF_REPO           ="https://github.com/PowerScript/KatanaFramework/"
KTF_LINCENSE       ="https://github.com/PowerScript/KatanaFramework/blob/master/doc/LICENCE"
TABLE_FOLDER_ADMIN ="files/db/commons-dir-admin.tbl"
DITIONARY_PASSWORDS="files/db/pass.dicc"
AGENTS_BROWSER     ="files/db/headersbrowser.list"
PATCH_INTALL       ="/usr/share/"
NMAP_PATH          ="/usr/bin/nmap"
"""Commons"""
LOCAL_IP           ="127.0.0.1"
INTERFACE_ETHERNET ="eth0"
INTERFACE_DEVICE   ="wlan0"
INTERFACE_MONITOR  ="wlan0mon"
MAC_TARGET         ="AA:A1:BB:B2:CC:C1"
CHANNEL_TARGET     ="9"
ESSID_TARGET       ="FUCK-ME"
MY_IP              ="192.168.1.225"
GATEWAY_ADR        ="192.168.1.254"
EMAIL              ="root@localhost"
USERNAME           ="root"
PASSWORD           ="toor"
"""Ports"""
FTP_PORT           ="21"
HTTP_PORT          ="80"
POP_PORT           ="110"
SQL_PORT           ="3306"
SSH_PORT           ="22"
SMTP_PORT          ="25"
# END DEFAULT VARIABLES
