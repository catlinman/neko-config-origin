nginx -s stop
letsencrypt certonly --expand --allow-subset-of-names --renew-by-default -a standalone \
	-d catlinman.com \
	-d nekodrop.catlinman.com \
	-d www.catlinman.com \
	-d dev.catlinman.com \
	-d netdata.catlinman.com \
	-d znc.catlinman.com \
	-d cloud.catlinman.com \
	-d ask.catlinman.com \
	-d twitter.catlinman.com \
	-d facebook.catlinman.com \
	-d youtube.catlinman.com \
	-d steam.catlinman.com \
	-d flickr.catlinman.com \
	-d instagram.catlinman.com \
	-d snapchat.catlinman.com \
	-d osu.catlinman.com \
	-d deviantart.catlinman.com \
	-d github.catlinman.com \
	-d googleplus.catlinman.com \
	-d cloud.catlinman.com
nginx
