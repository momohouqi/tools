# !/bin/bash

max_count_backup_files=30
backupFilename="/var/atlassian/application-data/confluence/backups/backup-*"
#backupFilename="/root/temp"

while countOfBackupFiles=$(ls ${backupFilename} | wc -l) && ((${countOfBackupFiles} > ${max_count_backup_files}))
do
    #echo "rm -rf ${backupFilename}\/$(ls -t ${backupFilename}| tail -n 1)"
    echo "rm -rf $(ls -t ${backupFilename}| tail -n 1)"
    rm -rf $(ls -t ${backupFilename}| tail -n 1)
    #sleep 1
done
