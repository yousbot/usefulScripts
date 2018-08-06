#!/bin/sh

# Created by Youssef Sbai Idrissi
# Version 1.0 
# This script do a full diagnostic of a specific server. It collects all the required elements such as : System, Network, Space ... 
# It generates a file global_system_info.zip on /tmp that contains all the required files. 
# It should have the right of executable : a+x 
 
        mkdir global_system_info
        cd global_system_info
        mkdir pdcollect-infos
        cd pdcollect-infos

        echo "Collecting environment information..."

                env > env.info 2>&1
                id >> env.info 2>&1
                ulimit -a  > ulimit.info 2>&1
                ulimit -Ha >> ulimit.info 2>&1

        echo "Collecting system information..."

                kudzu -p >> system.info  2>&1
                lspci >> system.info  2>&1
                free >>  system.info  2>&1
                hwinfo >> system.info 2>&1
                dmidecode >> system.info 2>&1
                cat /proc/cpuinfo >> system.info 2>&1
                cat /proc/meminfo  >> system.info  2>&1

        echo "Collecting bootup messages..."

                dmesg > dmesg.out 2>&1

        echo "Collecting release information..."

                cat /etc/*-release > release.out 2>&1

        echo "Collecting maintenance information..."

                rpm -qa --qf '[%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}\t%{INSTALLTIME:date}\n]' $*  > maint.info  2>&1

        echo "Collecting disk space information..."

                df -l > disk.info  2>&1

        echo "Collecting network information..."

                /sbin/ifconfig -a > ipconfig.info  2>&1
                netstat -a -n > netstat.info 2>&1
                netstat -a -r >> netstat.info 2>&1
                netstat -rCn  >> netstat.info 2>&1
                cp -p /etc/nsswitch.conf . 2>/dev/null
                cp -p /etc/hosts . 2>/dev/null
                cp -p /etc/resolv.conf . 2>/dev/null

        echo "Collecting running process information..."
                ps -efL >tasklist.info 2>&1

        echo "Collecting installed programs information..."

                touch programs.info
                IFS=: read -ra dirs_in_path <<< "$PATH"
                for dir in "${dirs_in_path[@]}"; do
                        for file in "$dir"/*; do
                                [[ -x $file && -f $file ]] && printf '%s\n' "${file##*/}" >> programs.info
                        done
                done

        echo "Collecting Versions information..."

                touch versions.info
                $(dirname $(dirname $(readlink -f $(which javac)))) >> versions.info  2>&1

        echo "Creating Zip file..."
        cd ..
        zip -r /tmp/global_system_info.zip pdcollect-infos

        echo "Cleaning Environment..."
        cd ..
        rm -rf global_system_info
        
        echo "Your info Zip is ready on : /tmp/global_system_info.zip"
        echo 'Find Weblogic Versions    : find / -name "*.product.properties" '
        




