kill -9 $(pidof uwsgi)
cd /var/www/vhosts/divorcesus.com/divorces
uwsgi --socket :8005 --module divorces.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root  --master --processes 6 --threads 3 --stats 127.0.0.1:9191 --daemonize=/var/www/vhosts/divorcesus.com/logs/uwsgi.log


