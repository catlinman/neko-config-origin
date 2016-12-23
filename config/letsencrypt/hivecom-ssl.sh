
nginx -s stop nginx -s stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d hivecom.net \
	-d www.hivecom.net \
	-d dev.hivecom.net \
	-d ts.hivecom.net \
	-d dc.hivecom.net

nginx # Restart the nginx server.
