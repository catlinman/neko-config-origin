nginx -s stop
letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d hivecom.net \
	-d www.hivecom.net \
	-d dev.hivecom.net \
	-d ts.hivecom.net \
	-d dc.hivecom.net
nginx
