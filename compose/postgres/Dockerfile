FROM postgres:12.4

#COPY ./init-user-db.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/init-user-db.sh
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
CMD ["docker-entrypoint.sh", "postgres"]
