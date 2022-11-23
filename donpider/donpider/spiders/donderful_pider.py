import scrapy

class DonderfulPider(scrapy.Spider):
    name = 'donderful'
    start_urls = [
        'https://dondafulfestival-20th.taiko-ch.net/en/music/songlist.php'
    ]


    def parse(self, response):
        for song in response.css('li.pops'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'pop_title': titles,
                'pop_subtitle': subtitles
            }

        for song in response.css('li.anime'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'anime_title': titles,
                'anime_subtitle': subtitles
            }

        for song in response.css('li.vocaloid'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'vocaloid_title': titles,
                'vocaloid_subtitle': subtitles
            }

        for song in response.css('li.variety'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'variety_title': titles,
                'variety_subtitle': subtitles
            }
        
        for song in response.css('li.classic'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'classical_title': titles,
                'classical_subtitle': subtitles
            }

        for song in response.css('li.game'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'game_title': titles,
                'game_subtitle': subtitles
            }

        for song in response.css('li.namco'):
            titles = song.css('dt.song::text').getall()
            for title in titles:
                title = title.encode('utf-8').decode('unicode-escape')

            subtitles = list(map(
                lambda x: x.replace('<dd>', ''), 
                song.css('dd').getall()
            ))
            subtitles = list(map(
                lambda x: x.replace('</dd>', ''), 
                subtitles
            ))
            for subtitle in subtitles:
                subtitle = subtitle.encode('utf-8').decode('unicode-escape')

            yield {
                'namco_title': titles,
                'namco_subtitle': subtitles
            }
