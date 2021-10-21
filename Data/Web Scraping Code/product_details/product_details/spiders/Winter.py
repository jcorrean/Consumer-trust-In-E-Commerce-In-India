import scrapy
class ProductDetailsItem(scrapy.Spider):
    name="Winter"
    allowed_domains= ['www.flipkart.com']
    start_urls=[]#Link1
    def parse(self, response):
            yield { 
                'Title':response.css('span[class="B_NuCI"]::text').get(),
                'Price':response.css('div[class="_30jeq3 _16Jk6d"]::text').get().replace(',','').replace('(','').replace(')','').replace('₹',''),
                'Number_of_ratings':response.css('span[class="_2_R_DZ"]::text').get().replace(',','').replace('(','').replace(')',''),
                'Avg_rating':response.css('div[class="_2d4LTz"]::text').get(),
                '5':response.css('div[class="_1uJVNT"]::text')[0].get().replace(',',''),
                '4':response.css('div[class="_1uJVNT"]::text')[1].get().replace(',',''),
                '3':response.css('div[class="_1uJVNT"]::text')[2].get().replace(',',''),
                '2':response.css('div[class="_1uJVNT"]::text')[3].get().replace(',',''),
                '1':response.css('div[class="_1uJVNT"]::text')[4].get().replace(',',''),
            }
            lst1=['''List of Links
                  ''']
            for i in lst1:
                yield scrapy.Request(i,callback=self.parse)