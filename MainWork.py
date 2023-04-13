import requests
from random import choice

class CheckEmail:
    def __init__(self, language, proxy=None, type_proxy=None):
        self.proxy = proxy
        self.type_proxy = type_proxy
        self.language = language
        self.url = 'https://bitmoji.api.snapchat.com/api/user/find'
        if self.type_proxy == 'socks5':
            proxies = {
                "http": "socks5://"+self.proxy,
                "https": "socks5://"+self.proxy
            }
            self.proxies = proxies
        elif self.type_proxy == 'http' or "https":
            proxies = {
                "http": self.proxy,
                "https": self.proxy
            }
            self.proxies = proxies
            
        elif self.type_proxy is None:
            self.proxies = None
            
        else:
            print(language['proxy_type_error'])
            exit()
    
    def get_information(self, email):
        data = {'email': email}
        headers = {"User-Agent": self._random_useragent(), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}
        try:
            response = requests.post(self.url, headers=headers, data=data, proxies=self.proxies)
            information = self.create_message(response.json())
            return information
        except requests.exceptions.ConnectionError:
            print(self.language['any_error'])
        except requests.exceptions.JSONDecodeError:
            pass
    @staticmethod
    def create_message(json_data):
        match json_data:
            case {'account_type': 'snapchat'}:
                return 'snapchat'
            case {'account_type': 'bitmoji'}:
                return 'bitmoji'
            case {'statusCode': 429, 'error': 'Too Many Requests', 'message': 'Too Many Requests'}:
                return False
            case _:
                return None

    @staticmethod
    def _random_useragent():
        useragents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
            'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
            'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/']
        return choice(useragents)

