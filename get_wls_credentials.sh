#!/bin/bash

touch /tmp/decrypt_password.py

echo ""; echo "";
echo " DECRYPTING WEBLOGIC CREDENTIALS "
echo " Note : Run This script as Root "; echo ""; echo "";

echo " *************************************************************** "; echo "";

find / -name "setDomainEnv.sh"

echo ""
echo " *************************************************************** "; echo "";

read -p " Enter the appropriate setDomainEnv.sh file : " domainenv_var

source $domainenv_var

echo " *************************************************************** "; echo"";
find / -name "boot.properties"

echo ""
echo " *************************************************************** "; echo "";

read -p " Enter the appropriate boot.properties file : " bootprop_var ; echo"";
boot_prp_path=`find $DOMAIN_HOME/servers/ -name "boot.properties" -print`

wls_usr=`grep username $boot_prp_path | sed -e "s/^username=\(.*\)/\1/"`
wls_pwd=`grep password $boot_prp_path | sed -e "s/^password=\(.*\)/\1/"`

echo " Encrypted Weblogic Username : $wls_usr "
echo " Encrypted Weblogic Password : $wls_pwd "; echo "";

echo " *************************************************************** "; echo "";
cat <<EOT >/tmp/decrypt_password.py
from weblogic.security.internal import *
from weblogic.security.internal.encryption import *
encryptionService = SerializedSystemIni.getEncryptionService(".")
clearOrEncryptService = ClearOrEncryptedService(encryptionService)
usr = str('$wls_usr')
pwd = str('$wls_pwd')
print "\n\n\n "
print " ************************************** \n\n"
print "  Username   :   " + clearOrEncryptService.decrypt(usr)
print "  Password   :   " + clearOrEncryptService.decrypt(pwd)
print " \n\n"
print " ************************************** \n\n"
EOT
cd $DOMAIN_HOME/security/
echo ""; echo "";
java weblogic.WLST /tmp/decrypt_password.py $wls_usr
rm -rf /tmp/decrypt_password.py;
