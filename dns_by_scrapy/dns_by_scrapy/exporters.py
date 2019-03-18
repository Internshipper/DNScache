# -*- coding: utf-8 -*-

# define output formation

from scrapy.exporters import CsvItemExporter


class HostItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['include_headers_line'] = False
        kwargs['delimiter'] = '\t'
        super(HostItemExporter, self).__init__(*args, **kwargs)
        self.fields_to_export = ['ip', 'name']
