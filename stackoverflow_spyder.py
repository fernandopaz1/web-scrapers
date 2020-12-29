from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item) :
    pregunta = Field()
    id = Field()

class StackOverFlowSpider(Spider) :
    name = "stackOverflowScraper"
    start_urls = ['https://stackoverflow.com/questions']
    def parse(self, response) :
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]/div')
        print(preguntas)
        
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_value('id', i)
            yield item.load_item()