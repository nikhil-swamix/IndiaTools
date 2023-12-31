docker pull odoo
docker pull postgres
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=postgres --name db postgres
docker run -p 8069:8069 --name odoo --link db:db -t odoo