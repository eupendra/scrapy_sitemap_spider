from scrapy.spiders import SitemapSpider
from scrapy.shell import inspect_response


# # Example 1
# class IqunixSpider(SitemapSpider):
#     name = 'iqunix'
#     sitemap_urls = ['https://iqunix.store/sitemap_products_1.xml?from=4505724289084&to=7097643204668']


#     def parse(self, response):
# yield {
#     'product': response.css('.product_title::Text').get(),
#     'price': response.css('#price_ppr .money::Text').get(),
# }


# # Example 2
# class IqunixSpider(SitemapSpider):
#     name = 'iqunix'
#     sitemap_urls = ['https://iqunix.store/sitemap.xml']
#     sitemap_follow = ['/sitemap_products']

#     def parse(self, response):
#         yield {
#             'product': response.css('.product_title::Text').get(),
#             'price': response.css('#price_ppr .money::Text').get(),
#         }


# Example 3
class IqunixSpider(SitemapSpider):
    name = 'iqunix'
    sitemap_urls = ['https://iqunix.store/sitemap.xml']
    sitemap_follow = ['/sitemap_products', 'blog']

    sitemap_rules = [
        ('/blogs', 'parse_blogs'),
        ('/products', 'parse_product'),
    ]

    def parse_product(self, response):
        yield {
            'product': response.css('.product_title::Text').get(),
            'price': response.css('#price_ppr .money::Text').get(),
        }

    def parse_blogs(self, response):
        yield {
            'title':  ''.join(response.xpath('(//*[@data-pf-type="Heading"])[1]//text()').getall()),
        }


