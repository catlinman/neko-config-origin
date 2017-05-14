
/etc/init.d/nginx stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

certbot certonly --standalone --renew-by-default --expand \
	-d quotic.net \
	-d www.quotic.net \
	-d dev.quotic.net

/etc/init.d/nginx start # Restart the nginx server.

