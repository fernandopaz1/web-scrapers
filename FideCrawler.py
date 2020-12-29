from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class PlayerItem(Item):
    nombre = Field()
    puesto = Field()
    rating = Field()

class FideCrawler(CrawlSpider):
    name = "MiPimerCrawling"
    start_urls = ["https://ratings.fide.com/top_federations.phtml"]
    allowed_domains = ['ratings.fide.com']  #Evita que se vaya de la pagina

    #Callback es la funcion que corre a ejecutar la regla en la que la llamo
    rules = (
        Rule(LinkExtractor(allow=r'country=')),
        Rule(LinkExtractor(allow=r'/profile/'), callback = 'parse_items')
    )

    def parse_items(self, response):
        item = ItemLoader(PlayerItem(), response)
        item.add_xpath('nombre', '/html/body/section[3]/b</div/div[1]/div/div[2]/div/div[1]/text()')
        item.add_xpath('puesto', '/html/body/section[3]/b</div/div[1]/div/div[2]/div/div[4]/div[1]/div[1]/div[2]/text()')
        item.add_xpath('rating', '/html/body/section[3]/b</div/div[1]/div/div[2]/div/div[5]/div/div[2]/div[1]/text()')
        yield item