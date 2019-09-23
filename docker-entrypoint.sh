#!/bin/bash
python3 /app/bin/splash --proxy-profiles-path /etc/splash/proxy-profiles --js-profiles-path /etc/splash/js-profiles--filters-path /etc/splash/filters --lua-package-path /etc/splash/lua_modules/?.lua &

cd ./src

scrapy crawl yelp_spider