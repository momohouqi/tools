!/bin/bash

fileName=$(/bin/ls -t /var/atlassian/application-data/confluence/backups/backup-* | head -n 1)
./scp_then_input_password.expect $fileName
