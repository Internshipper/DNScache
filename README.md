DNS cache

# make hostname list file
Firefox->Library->History->Show All History->Views->Only Name and Location->Ctrl+A->Ctrl+C
$ python extract_hostname.py -if CtrlVfilename -of dn.list

# batch DNS to generate hosts
dns_by_scrapy	get batch DNS from cloudflare via scrapy
* [Usage](dns_by_scrapy/README.md)