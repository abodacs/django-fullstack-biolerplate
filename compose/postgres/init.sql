CREATE USER postgres SUPERUSER;
CREATE DATABASE postgres WITH OWNER postgres;
CREATE USER online_benevolent;
CREATE DATABASE online_benevolent_dev;
GRANT ALL PRIVILEGES ON DATABASE online_benevolent_dev TO online_benevolent;
