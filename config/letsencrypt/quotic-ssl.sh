nginx -s stop
letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d quotic.net \
	-d www.quotic.net \
	-d dev.quotic.net
nginx
