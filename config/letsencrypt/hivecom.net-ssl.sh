
/etc/init.d/nginx stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

certbot certonly --expand --renew-by-default --standalone \
	-d hivecom.net \
	-d www.hivecom.net \
	-d dev.hivecom.net \
	-d ts.hivecom.net \
	-d dc.hivecom.net

/etc/init.d/nginx start # Restart the nginx server.

