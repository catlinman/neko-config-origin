
nginx -s stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d mavulp.com \
	-d www.mavulp.com \
	-d dev.mavulp.com \
	-d roflbox.mavulp.com

nginx # Restart the nginx server.
