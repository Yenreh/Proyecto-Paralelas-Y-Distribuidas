FROM mariadb:latest

COPY init.sql /docker-entrypoint-initdb.d/

RUN mariadb  < /docker-entrypoint-initdb.d/init.sql
