"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import re
import urlparse
import random
from salts_lib import kodi
from salts_lib import log_utils
from salts_lib import scraper_utils
from salts_lib import dom_parser
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import QUALITIES
import scraper
import xml.etree.ElementTree as ET

try:
    from xml.parsers.expat import ExpatError
except ImportError:
    class ExpatError(Exception): pass
try:
    from xml.etree.ElementTree import ParseError
except ImportError:
    class ParseError(Exception): pass

BASE_URL = 'http://dizilab.com'
STREAM_URL = '%s%s|User-Agent=%s&Referer=%s'

class Dizilab_Scraper(scraper.Scraper):
    base_url = BASE_URL

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'Dizilab'

    def resolve_link(self, link):
        return link

    def format_source_label(self, item):
        label = '[%s] %s' % (item['quality'], item['host'])
        if 'subs' in item and item['subs']:
            label += ' (%s)' % (item['subs'])
        return label

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            page_url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(page_url, cache_limit=.5)
            page_urls = [page_url]
            if kodi.get_setting('scraper_url'):
                page_urls += self.__get_page_urls(html)
            
            for page_url in page_urls:
                html = self._http_get(page_url, cache_limit=.5)
                subs = 'Turkish Subtitles'
                fragment = dom_parser.parse_dom(html, 'li', {'class': 'active'})
                if fragment:
                    frag_class = dom_parser.parse_dom(fragment[0], 'span', ret='class')
                    if frag_class:
                        if frag_class[0] == 'icon-en':
                            subs = 'English Subtitles'
                        elif frag_class[0] == 'icon-orj':
                            subs = ''
                            
                hosters += self.__get_cloud_links(html, page_url, subs)
                hosters += self.__get_embedded_links(html, subs)
                hosters += self.__get_iframe_links(html, subs)

        return hosters

    def __get_page_urls(self, html):
        page_urls = []
        for item in dom_parser.parse_dom(html, 'li', {'class': ''}):
            page_url = dom_parser.parse_dom(item, 'a', ret='href')
            if page_url:
                page_urls.append(page_url[0])
        return page_urls
    
    def __get_iframe_links(self, html, subs):
        hosters = []
        iframe_urls = dom_parser.parse_dom(html, 'iframe', {'id': 'episode_player'}, ret='src')
        if iframe_urls:
            stream_url = iframe_urls[0]
            host = urlparse.urlparse(stream_url).hostname
            quality = QUALITIES.HD720
            if host:
                hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': False}
                hoster['subs'] = subs
                hosters.append(hoster)
        return hosters
    
    def __get_embedded_links(self, html, subs):
        hosters = []
        sources = self._parse_sources_list(html)
        for source in sources:
            host = self._get_direct_hostname(source)
            quality = sources[source]['quality']
            direct = sources[source]['direct']
            hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': source, 'direct': direct}
            hoster['subs'] = subs
            hosters.append(hoster)
        return hosters
    
    def __get_cloud_links(self, html, page_url, subs):
        hosters = []
        match = re.search("dizi_kapak_getir\('([^']+)", html)
        if match:
            ep_id = match.group(1)
            for script_url in dom_parser.parse_dom(html, 'script', {'data-cfasync': 'false'}, ret='src'):
                html = self._http_get(script_url, cache_limit=24)
                match1 = re.search("var\s+kapak_url\s*=\s*'([^']+)", html)
                match2 = re.search("var\s+aCtkp\s*=\s*'([^']+)", html)
                if match1 and match2:
                    link_url = '%s?fileid=%s&access_token=%s' % (match1.group(1), ep_id, match2.group(1))
                    headers = {'Referer': page_url}
                    html = self._http_get(link_url, headers=headers, cache_limit=.5)
                    js_data = scraper_utils.parse_json(html, link_url)
                    if 'variants' in js_data:
                        for variant in js_data['variants']:
                            if 'hosts' in variant and variant['hosts']:
                                stream_host = random.choice(variant['hosts'])
                                stream_url = STREAM_URL % (stream_host, variant['path'], scraper_utils.get_ua(), page_url)
                                if not stream_url.startswith('http'):
                                    stream_url = 'http://' + stream_url
                                host = self._get_direct_hostname(stream_url)
                                if 'width' in variant:
                                    quality = scraper_utils.width_get_quality(variant['width'])
                                elif 'height' in variant:
                                    quality = scraper_utils.height_get_quality(variant['height'])
                                else:
                                    quality = QUALITIES.HIGH
                                hoster = {'multi-part': False, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': True}
                                hoster['subs'] = subs
                                hosters.append(hoster)
        return hosters
    
    def get_url(self, video):
        return self._default_get_url(video)

    def _get_episode_url(self, show_url, video):
        episode_pattern = 'class="episode"\s+href="([^"]+/sezon-%s/bolum-%s)"' % (video.season, video.episode)
        title_pattern = 'class="episode-name"\s+href="(?P<url>[^"]+)">(?P<title>[^<]+)'
        return self._default_get_episode_url(show_url, video, episode_pattern, title_pattern)

    def search(self, video_type, title, year, season=''):
        results = []
        xml_url = urlparse.urljoin(self.base_url, '/diziler.xml')
        xml = self._http_get(xml_url, cache_limit=24)
        if xml:
            norm_title = scraper_utils.normalize_title(title)
            match_year = ''
            try:
                for element in ET.fromstring(xml).findall('.//dizi'):
                    name = element.find('adi')
                    if name is not None and norm_title in scraper_utils.normalize_title(name.text):
                        url = element.find('url')
                        if url is not None and (not year or not match_year or year == match_year):
                            result = {'url': scraper_utils.pathify_url(url.text), 'title': scraper_utils.cleanse_title(name.text), 'year': ''}
                            results.append(result)
            except (ParseError, ExpatError) as e:
                log_utils.log('Dizilab Search Parse Error: %s' % (e), log_utils.LOGWARNING)

        return results
