# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinainfoPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将/替换为_,保存为.txt
        filename = sonUrls[7:-6].replace('/', '_')
        filename += ".txt"

        fp = open(item['subFilename']+'/'+filename, 'w')
        fp.write(item['content'])
        fp.close()
        return item