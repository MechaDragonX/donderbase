import scrapy

class DonderfulPider(scrapy.Spider):
    name = 'donderful'
    start_urls = [
        'https://dondafulfestival-20th.taiko-ch.net/en/music/songlist.php'
    ]

    def parse(self, response):
        for song in response.css('li.pops'):
            yield {
                'pop_title': song.css('dt.song::text').getall(),
                'pop_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
        for song in response.css('li.anime'):
            yield {
                'anime_title': song.css('dt.song::text').getall(),
                'anime_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
        for song in response.css('li.vocaloid'):
            yield {
                'vocaloid_title': song.css('dt.song::text').getall(),
                'vocaloid_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }

        for song in response.css('li.variety'):
            yield {
                'variety_title': song.css('dt.song::text').getall(),
                'variety_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
        for song in response.css('li.classic'):
            yield {
                'classical_title': song.css('dt.song::text').getall(),
                'classical_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
        for song in response.css('li.game'):
            yield {
                'game_title': song.css('dt.song::text').getall(),
                'game_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
        for song in response.css('li.namco'):
            yield {
                'namco_title': song.css('dt.song::text').getall(),
                'namco_subtitle': list(map(
                    lambda x: x.replace('<dd></dd>', ''), 
                    song.css('dd').getall()
                ))
            }
