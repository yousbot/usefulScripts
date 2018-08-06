# useful_linux_scripts
This is a random collection of linux scripts, for system administration, software integration and so on. 

## System Diagnostic 
This script gives you a full diagnostic of your system, including the RAM, CPU, DISK, Installed Programs, RPMS, ... 
Tested on RHEL 7.4 

```sh
# Run it as follow 
wget https://raw.githubusercontent.com/sbaiidrissiyoussef/useful_linux_scripts/master/General_System_Infos.sh
chmod 777 General_System_Infos.sh
./General_System_Infos.sh

```
## Get Weblogic Credentials
Gives you the credentials of your Weblogic Application Server. Must be run as root. 
Tested on RHEL 7.4 and Weblogic Application Server 10.3.6

```sh
# Run it as follow 
wget https://raw.githubusercontent.com/sbaiidrissiyoussef/useful_linux_scripts/master/get_wls_credentials.sh
chmod 777 get_wls_credentials.sh
./get_wls_credentials.sh

```
