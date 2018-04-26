from scrapy import cmdline


cmdline.execute("scrapy crawl example -o items.json".split())
