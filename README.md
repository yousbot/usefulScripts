# Useful Linux Scripts

![Still in Progress](https://img.shields.io/badge/Progress-Still%20in%20Progress-blue)

This repository contains a collection of Linux scripts that are useful for system administration, software integration, and various other tasks.

## Table of Contents
- [Simulate File Decompression](#simulate-file-decompression)
- [Convert JSONL to JSON](#convert-jsonl-to-json)
- [System Diagnostic](#system-diagnostic)
- [Get Weblogic Credentials](#get-weblogic-credentials)
- [Project Details](#project-details)

---
## Simulate File Decompression
A Python script to estimate the uncompressed size of compressed files without actually decompressing them.
*Supported formats : gz, zip, tar, bz2, xz.*

**To run the script, execute the following command:**
```bash
python simulate_decompression.py <file_path>
```
---
## Convert JSONL to JSON

This scripts aims to convert JSONL files into JSON files, in the most optimum way. It works on very large files and datasets( > 20 GB )

**To run the script, execute the following command:**
```bash
python convert_jsonl_to_json.py <JSONL_File_Path> <JSON_File_Path> <Buffer_Size>
```

---
## System Diagnostic

This script provides a comprehensive diagnostic of your system, covering RAM, CPU, Disk, Installed Programs, RPMS, and more. It has been tested on RHEL 7.4.

**To run the script, execute the following commands:**

```bash
wget https://raw.githubusercontent.com/sbaiidrissiyoussef/useful_linux_scripts/master/General_System_Infos.sh
chmod 777 General_System_Infos.sh
./General_System_Infos.sh
```

---

## Get Weblogic Credentials

This script retrieves the credentials of your Weblogic Application Server. It must be run as root and has been tested on RHEL 7.4 and Weblogic Application Server 10.3.6.

**To run the script, execute the following commands:**

```bash
wget https://raw.githubusercontent.com/sbaiidrissiyoussef/useful_linux_scripts/master/get_wls_credentials.sh
chmod 777 get_wls_credentials.sh
./get_wls_credentials.sh
```

---

## Project Details

- **Author**: Youssef Sbai Idrissi
- **Version**: 0.1.0
