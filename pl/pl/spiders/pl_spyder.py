import scrapy
from ..items import PlItem

class pl_spyder(scrapy.Spider):
    name = "teams"
    start_urls = [
        'https://www.skysports.com/premier-league-results'
    ]
    def parse(self, response):
        items = PlItem()
        mathc_20 = response.css("span.swap-text__target::text").extract()
        scores_20=response.css("span.matches__teamscores-side::text").extract()

        items['mathc_20'] =mathc_20
        items['scores_20']= scores_20

        yield items