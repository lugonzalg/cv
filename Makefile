COMPOSE=docker compose -f srcs/docker-compose.yml
DOMAIN=ikerketa.com

certs:
	$(COMPOSE) down certbot
	$(COMPOSE) run --rm certbot certonly --webroot --webroot-path=/var/www/certbot -d $(DOMAIN) -d www.$(DOMAIN)
