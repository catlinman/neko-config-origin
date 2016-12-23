
nginx -s stop # Stop the nginx server as it is listening on port 80 which is used by standalone verification.

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

nginx # Restart the nginx server.

# ZNC certificate transfer.
cat /etc/letsencrypt/live/catlinman.com/privkey.pem > .znc/znc.pem
cat /etc/letsencrypt/live/catlinman.com/cert.pem >> .znc/znc.pem
