import scrapy
class FlipkartreviewsItem(scrapy.Spider):
    Page_No=1
    name="Summer"
    allowed_domains= ['www.flipkart.com']
    # Ex of start url = https://www.flipkart.com/home-sizzler-214-cm-7-ft-polyester-door-curtain-pack-2/product-reviews/itmf3xnh3cmhccxh?pid=CRNETWY9JXF8URMU&lid=LSTCRNETWY9JXF8URMUD22M0V&marketplace=FLIPKART&page=1
    start_urls=[""]
    
    def parse(self,response):
        for review in response.css('div[class=_27M-vq]'):
            r1=review.css('div[class="_3LWZlK _1BLPMq"]::text').get()
            r2=response.css('div[class="_3LWZlK _32lA32 _1BLPMq"]::text').get()
            r3=response.css('div[class="_3LWZlK _1rdVr6 _1BLPMq"]::text').get()
            if(r1):
                r=r1
            elif(r2):
                r=r2
            elif(r3):
                r=r3
            yield {
                'Rating':  r,
                'Heading': review.css('p[class="_2-N8zT"]::text').get(),
                'Detailed_review': review.css('div[class="t-ZTKy"] ::text').extract(),
                'Name': review.css('p[class="_2sc7ZR _2V5EHH"]::text').get(),
                'Time': review.css('p[class="_2sc7ZR"]::text').get(),
                'Upvotes':  review.css('span[class="_3c3Px5"]::text')[0].get(),
                'Downvotes': review.css('span[class="_3c3Px5"]::text')[1].get(),
                }
            '''
            # To parse till last page
        next_page =  response.css('a._1LKTO3::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)'''
            
            if FlipkartreviewsItem.Page_No <52: # 52 is Number of Pages
                FlipkartreviewsItem.Page_No +=1
            # next page id Ex - https://www.flipkart.com/home-sizzler-214-cm-7-ft-polyester-door-curtain-pack-2/product-reviews/itmf3xnh3cmhccxh?pid=CRNETWY9JXF8URMU&lid=LSTCRNETWY9JXF8URMUD22M0V&marketplace=FLIPKART&page=
            # Same as start url except remove last char 
            next_page_id=""+str(FlipkartreviewsItem.Page_No)
            next_page =response.urljoin(next_page_id)
            yield scrapy.Request(next_page,callback=self.parse)
