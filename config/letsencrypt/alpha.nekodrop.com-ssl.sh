
/etc/init.d/nginx stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

certbot certonly --standalone --renew-by-default --expand \
	-d nekodrop.com \
	-d www.nekodrop.com \
	-d alpha.nekodrop.com

/etc/init.d/nginx start # Restart the nginx server.

