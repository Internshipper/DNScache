# -*- coding: utf-8 -*-

# get DNS

import ipaddress
import json
import scrapy
import urllib


class CloudflareSpider(scrapy.Spider):
    name = 'cloudflare'
    query_url = 'https://cloudflare-dns.com/dns-query?name=%s&type=%s'
    header = {'accept': 'application/dns-json'}
    
    def start_requests(self):
        dn_list = [line.strip() for line in open('dn.list').readlines()]
        for dn in dn_list:
            yield scrapy.Request(url=self.query_url % (dn, 'AAAA'), callback=self.parse, method='GET', headers=self.header)

    def parse(self, response):
        if response.status == 200:
            request_url = urllib.parse.urlparse(response.request.url)
            query = urllib.parse.parse_qs(request_url.query)    #the value is list type
            q_name = query['name'][0]
            q_type = query['type'][0]
            body = json.loads(response.body)
            question = body.get('Question')[0]
            assert(question['name'][:len(q_name)] == q_name)    #name will be add a dot at the end
            answers = body.get('Answer', [])
            print('DEBUG:\n', query, q_name, q_type, question, '\nANS:', answers)
            for ans in answers:
                if ans.get('name') == question['name']:
                    try:
                        ipaddress.ip_address(ans.get('data'))
                    except:
                        continue
                    else:
                        yield {'name': q_name, 'ip': ans.get('data')}
                        return
            if q_type == 'AAAA':
                yield scrapy.Request(url=self.query_url % (q_name, 'A'), callback=self.parse, method='GET', headers=self.header)
