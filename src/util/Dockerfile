FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python3-pip python3-dev cron util-linux cifs-utils

COPY ./ ./util
WORKDIR ./util
RUN pip3 install -r requirements.txt

RUN chmod +x update_db.sh
RUN mkdir -p /mnt/tracker
COPY update-db-cron /etc/cron.d/update-db-cron
RUN chmod 0644 /etc/cron.d/update-db-cron
RUN touch /var/log/cron_logfile
RUN crontab /etc/cron.d/update-db-cron
CMD cron && tail -f /var/log/cron_logfile

