# CSS Selectors

title=response.css('span[class="B_NuCI"]::text').get()

price=response.css('div[class="_30jeq3 _16Jk6d"]::text').get().replace(',','').replace('(','').replace(')','').replace('₹','')

number_of_ratings=response.css('span[class="_2_R_DZ"]::text').get().replace(',','')

avg_rating=response.css('div[class="_2d4LTz"]::text').get()

5=response.css('div[class="_1uJVNT"]::text')[0].get().replace(',','')

4=response.css('div[class="_1uJVNT"]::text')[1].get().replace(',','')

3=response.css('div[class="_1uJVNT"]::text')[2].get().replace(',','')

2=response.css('div[class="_1uJVNT"]::text')[3].get().replace(',','')

1=response.css('div[class="_1uJVNT"]::text')[4].get().replace(',','')


# To run the scraper on Terminal 

scrapy crawl Winter -o overview.xlsx