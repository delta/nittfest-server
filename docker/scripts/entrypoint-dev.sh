#!/bin/sh

until nc -z -v -w30 db 3306
do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 5
done

echo -e "\e[34m >>> Running migrations \e[97m"
alembic upgrade head
if [ $? -eq 0 ]; then
    echo -e "\e[32m >>> Migration successful \e[97m"
else
    echo -e "\e[31m >>> Migration failed \e[97m"
    exit 1
fi

echo -e "\e[34m >>> Starting the server \e[97m"
uvicorn server.main:app --host 0.0.0.0 --reload