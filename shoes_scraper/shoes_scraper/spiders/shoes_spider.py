import scrapy

class ShoesSpider(scrapy.Spider):

    name = "shoes"    
    
    def start_requests(self):
        dict_list = [{'brand' : 'Air Jordan', 'url' : 'https://larrydeadstock.com/3-air-jordan'},
        {'brand' : 'Nike', 'url' : 'https://larrydeadstock.com/6-nike'},
        {'brand' : 'Adidas', 'url' : 'https://larrydeadstock.com/9-adidas'},
        {'brand' : 'Yeezy', 'url' : 'https://larrydeadstock.com/10-yeezy'},
        {'brand' : 'New Balance', 'url' : 'https://larrydeadstock.com/77-new-balance'},
        {'brand' : 'Asics', 'url' : 'https://larrydeadstock.com/79-asics'},
        {'brand' : 'Vans', 'url' : 'https://larrydeadstock.com/75-vans'},
        {'brand' : 'Reebok', 'url' : 'https://larrydeadstock.com/76-reebok'},
        {'brand' : 'Crocs', 'url' : 'https://larrydeadstock.com/91-crocs'}]

        for dictionnary in dict_list:
            yield scrapy.Request(dictionnary['url'], callback=self.catalog_parser,
            cb_kwargs={'brand': dictionnary['brand']})

    def catalog_parser(self, response, brand):

        # Look for links to specific product pagess
        url_specific_product_list = response.css('div.p-name h4 a::attr(href)').getall()

        for url_specific_product in url_specific_product_list: # Go to each product page
            yield scrapy.Request(url_specific_product, callback=self.product_parser,
            cb_kwargs={'brand': brand})

        next_page = response.css('a.next::attr(href)').get() # Go to next catalog page
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.catalog_parser, cb_kwargs={'brand': brand})

    def product_parser(self, response, brand): # Extract information for one product
       
        name = response.css('h1::text').get()
        link = response.url
        picture_links = response.css('div a img::attr(src)').getall()[2:] 
        sizes = response.css('div.product-variants select.form-control option::attr(title)').getall()
        brand = brand

        price = response.css('div.current-price span::attr(content)').get()
        price = float(price)

        description = response.css('div.card-block p::text').get()
        if description.startswith('Pas de commentaire'):
            description = ''

        return {'brand' : brand, 'name': name, 'price': price, 'sizes': sizes,
                'picture_links': picture_links, 'description': description, 'link': link}