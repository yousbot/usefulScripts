
# TSM 8.1 Migration Guide: Windows to Linux

## Overview

**Subject**: Notes on the migration of TSM 8.1 from a Windows server to a Linux server  
**Creator**: Youssef Sbai Idrissi, Data Engineer  
**Date**: 10/09/2019  

> **Note**: This guide assumes that TSM 8.1 supports migration from Windows to Linux. For the most up-to-date information, consult IBM's official documentation.

---

## Steps

### 1. Export DDL Schema from Database
```bash
db2look -d tsmdb1 -createdb -a -e -m -l -x -f -o TSMDB1_MONKEYS.ddl -td "@"
```

### 2. Export Data from Database

```bash
db2move tsmdb1 export -aw -u Administrateur -p P@ssw0rd
```

> **Action**: Move the exported Schema & DDL to the destination server.

### 3. Modify DDL File

- Replace "Administrateur" with "TSNINST1"

```bash
:%s/ADMINISTRATEUR/TSMINST1
```

- Update the paths as necessary.

### 4. Remove Existing Database

```bash
dsmserv removedb tsmdb1
```

> **Troubleshooting**: In case of issues, execute the following commands:

```bash
db2 quiesce db immediate
db2 force application all
db2 drop database tsmdb1
```

### 5. Format TSM Database

> **Note**: Directories must be empty.

```bash
dsmserv format dbdir=/tsm/tsmdb/001,/tsm/tsmdb/002,/tsm/tsmdb/003,/tsm/tsmdb/004              activelogdirectory=/tsm/tsmlog              archlogdirectory=/tsm/tsmarchlog              archfailoverlogdirectory=/tsm/tsmarchlogfailover              mirrorlogdirectory=/tsm/tsmmirrorlog
```

### 6. Import DDL Schema to Database

```bash
db2 -td@ -vf TSMDB1_MONKEYS.ddl
```

### 7. Import Data to Database

```bash
db2move DB_NAME_TARGET load -lo REPLACE > load.txt
```

### 8. Remove Pending State

```bash
db2 -x "select 'SET INTEGRITY FOR '||rtrim(creator)||'.'||rtrim(name)|| ' IMMEDIATE CHECKED;' from sysibm.systables where status='C' and creator not like 'SYS%' and type='T'" > integrity.txt
db2 -tvf integrity.txt
dsmserv
```

---

## End of Guide
