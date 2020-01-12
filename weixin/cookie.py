import requests
from weixin.config import *


class CookiePool:
    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError as e:
            print(e)
            return None

    def search_keywords(self):
        key = 'a'
        return key

    def get_cookie(self):
        """请求指定网站并获取cookie"""
        ip_proxy = self.get_proxy()
        query = self.search_keywords()
        header = {
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept - Language': 'zh - CN, zh;q = 0.9',
                'Connection': 'keep - alive',
                'cookie': '',
                'Host': 'weixin.sogou.com',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117 Safari / 537.36'
        }
        params = {
            'type': 2,
            'query': query
        }
        if ip_proxy is not None:
            result = requests.get("https://weixin.sogou.com/weixin", headers = header, params=params)
            print(result.status_code)
            if result.status_code == 200 and '需要您协助验证' not in result.text:
                print(result.cookies)


if __name__ == "__main__":
    cookie = CookiePool()
    print(cookie.get_proxy())
    print(cookie.get_cookie())