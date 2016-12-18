nginx -s stop
letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d tradrec.com \
	-d www.tradrec.com \
	-d dev.tradrec.com
nginx
