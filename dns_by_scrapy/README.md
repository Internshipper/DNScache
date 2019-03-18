Dns by Scrapy
=============

* First, prepare a dn.list file in the dir, which one line write a hostname.
* If there is a hosts file in the dir, remove it.
* Then run the commandline.
``` bash
scrapy crawl cloudflare -o hosts -t hosts
sudo mv hosts /etc/
```