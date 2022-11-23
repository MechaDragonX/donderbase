import scrapy

class DonderfulPider(scrapy.Spider):
    name = 'donderful'
    start_urls = [
        f'file:////{__file__.removesuffix("donpider/donpider/spiders/donderful_pider.py")}data/donderful.html'
    ]

    def parse(self, response):
        for song in response.css('li.pops'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'pop_title': title,
                'pop_subtitle': subtitle
            }

        for song in response.css('li.anime'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'anime_title': title,
                'anime_subtitle': subtitle
            }

        for song in response.css('li.vocaloid'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'vocaloid_title': title,
                'vocaloid_subtitle': subtitle
            }

        for song in response.css('li.variety'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'variety_title': title,
                'variety_subtitle': subtitle
            }
        
        for song in response.css('li.classic'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'classical_title': title,
                'classical_subtitle': subtitle
            }

        for song in response.css('li.game'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'game_title': title,
                'game_subtitle': subtitle
            }

        for song in response.css('li.namco'):
            title = self.extract_title(song)
            subtitle = self.extract_subtitle(song)

            yield {
                'namco_title': title,
                'namco_subtitle': subtitle
            }

    def extract_title(self, song):
        titles = song.css('dt.song::text').getall()
        for title in titles:
            title = title.encode('utf-8').decode('unicode-escape')
        
        if len(titles) == 1:
            return titles[0]
        return self.remove_breaks(titles)

    def extract_subtitle(self, song):
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

        if len(subtitles) == 1:
                return subtitles[0]
        return self.remove_breaks(subtitles)
    def remove_breaks(self, list):
        result = ''
        i = 0
        while i < len(list):
            if i != len(list) - 1:
                result += f'{list[i]} '
            else:
                result += list[i]
            i += 1
        return result
