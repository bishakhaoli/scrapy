import scrapy



class CountriesSpider(scrapy.Spider):
    name = "countries"
    start_urls = [
         'https://www.scrapethissite.com/pages/simple/'
    ]

    def parse(self, response):
        for country in response.css('div.col-md-4 country'):
            yield {
                'name': country.css('h3.country-name::text').get(),
                'capital': country.css('div.country-info span.country-capital::text').get(),
                'population': country.css('div.country-info span.country-population::text').get(),
                'area': country.css('div.country-info span.country-area::text').get(),
            }