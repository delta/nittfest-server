#!/bin/sh

docker exec nittfest_db /usr/bin/mysqldump -u root --password=password nittfest_db > scripts/backup/backup.sql
