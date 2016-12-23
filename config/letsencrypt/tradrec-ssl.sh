
nginx -s stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d tradrec.com \
	-d www.tradrec.com \
	-d dev.tradrec.com

nginx # Restart the nginx server.
