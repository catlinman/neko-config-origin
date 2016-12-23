
nginx -s stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d quotic.net \
	-d www.quotic.net \
	-d dev.quotic.net

nginx # Restart the nginx server.
