# CSS Selectors

all_reviews= response.css('div[class=_27M-vq]')

rating =  response.css('div[class="_3LWZlK _1BLPMq"]::text').get()

rating2 = response.css('div[class="_3LWZlK _32lA32 _1BLPMq"]::text').get()

rating3 =  response.css('div[class="_3LWZlK _1rdVr6 _1BLPMq"]::text').get()

heading = response.css('p[class="_2-N8zT"]::text').get()

detailed_review = response.css('div[class="t-ZTKy"] ::text').extract()

name = response.css('p[class="_2sc7ZR _2V5EHH"]::text').get()

time = response.css('p[class="_2sc7ZR"]::text').get()

upvotes = response.css('span[class="_3c3Px5"]::text')[0].get()

downvotes = response.css('span[class="_3c3Px5"]::text')[1].get()

# To run the scraper on Terminal 

scrapy crawl Summer -o output.xlsx