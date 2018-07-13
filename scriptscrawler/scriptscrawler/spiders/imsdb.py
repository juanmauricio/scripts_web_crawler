import scrapy

class IMSDBSpider(scrapy.Spider):
    name = "IMSDB"

def start_requests(self):
    urlsMoviesByLetter= [
        'http://www.imsdb.com/alphabetical/0',
        'http://www.imsdb.com/alphabetical/A',
        'http://www.imsdb.com/alphabetical/B',
        'http://www.imsdb.com/alphabetical/C',
        'http://www.imsdb.com/alphabetical/D'
    ]

    for url in urlsMoviesByLetter:
        yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
    # Obtiene la lista de urls para la letra especifica
    # http://www.imsdb.com/Movie%20Scripts/A%20Few%20Good%20Men%20Script.html

    # Busca todos los elementos a con href incluyendo 'Movie Scripts', cada uno corresponde a una pelicula con enlace al script.
    urlsMovieNamesByLetter = response.xpath('//p/a/@href').extract()

    for url in urlsMovieNamesByLetter:
        url = 'http://www.imsdb.com' + url
        yield scrapy.Request(url=url, callback=self.parse2)


def parse2(self, response):
     #Obtiene la info de la segunda hoja.

     #Llama, finalmente, el url que contiene el texto del script.
     #http://www.imsdb.com/scripts/A-Few-Good-Men.html
    urlWithScript = 

