import scrapy

class DonderfulPider(scrapy.Spider):
    name = 'donderful'
    start_urls = [
        f'file:////{__file__.removesuffix("donpider/donpider/spiders/donderful_pider.py")}donderbase/data/donderful.html'
    ]

    def extractTitles(self, song):
        titles = song.css('dt.song::text').getall()
        for title in titles:
            title = title.encode('utf-8').decode('unicode-escape')
        return titles
    def extractSubtitles(self, song):
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
        return subtitles

    def parse(self, response):
        for song in response.css('li.pops'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'pop_title': titles,
                'pop_subtitle': subtitles
            }

        for song in response.css('li.anime'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'anime_title': titles,
                'anime_subtitle': subtitles
            }

        for song in response.css('li.vocaloid'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'vocaloid_title': titles,
                'vocaloid_subtitle': subtitles
            }

        for song in response.css('li.variety'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'variety_title': titles,
                'variety_subtitle': subtitles
            }
        
        for song in response.css('li.classic'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'classical_title': titles,
                'classical_subtitle': subtitles
            }

        for song in response.css('li.game'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'game_title': titles,
                'game_subtitle': subtitles
            }

        for song in response.css('li.namco'):
            titles = self.extractTitles(song)

            subtitles = self.extractSubtitles(song)

            yield {
                'namco_title': titles,
                'namco_subtitle': subtitles
            }
