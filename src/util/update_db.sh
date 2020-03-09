#! /bin/bash

dir="/mnt/tracker/"

if mountpoint -q -- "$dir";then
    printf '%s\n' "$dir it's already mounted, proceeding with updates"
else
    printf '%s\n' "$dir Mounting directory..."
    mount -t cifs //192.168.16.2/logins -o username=cinfoadmin,password=admin2019 "$dir"
fi

echo "Updating database"
/usr/bin/python3 /util/update_db.py
