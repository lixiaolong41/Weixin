import requests
from weixin.config import *
import pickle

class CookiePool:
    def __init__(self):
        self.header = {
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
        self.cookie = "SUV=00EFA14877A388755DCBFC6F42791239; ABTEST=0|1576923887|v1; IPLOC=CN3701; SUID=EF22A2773E18960A000000005DFDF2EF; SUID=EF22A2772B12960A000000005DFDF2EF; weixinIndexVisited=1; LSTMV=248%2C70; LCLKINT=6981; ppinf=5|1578919400|1580129000|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTglQjclQUYlRTUlQkYlODN8Y3J0OjEwOjE1Nzg5MTk0MDB8cmVmbmljazoxODolRTglQjclQUYlRTUlQkYlODN8dXNlcmlkOjQ0Om85dDJsdUNYR1JOMmdPRHRrR1I4ZTRBZmhZY1lAd2VpeGluLnNvaHUuY29tfA; pprdig=TKrQbsDZrQfrPMnjD8nj3yQ8LpvQ5zlUN-dS3Wg58i3NI_GZgALhdqVciXoGvmz6XQKd8amnxvC1dQNYBDvq8twM30D1Tm3rmYVMahozwkw_pWTksxPk7xee0GLKF9bkZwmT_KhSa7Eq3eQTA_GmBc-H70hcOIz9Y9Hf8_YM104; sgid=22-44807557-AV4cZehG2egZO7crLzXO8og; ppmdig=157891940000000066a166a8e1a159029db8410e29079182; sct=4; SNUID=70C04491E5E379E2367A51C4E626F5C1; JSESSIONID=aaaAAafR3J2mNc2Ux9p_w".split(
            ";")
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
        cookie = {}
        ip_proxy = self.get_proxy()
        query = self.search_keywords()
        session = requests.Session()
        for i in self.cookie:
            key, value = i.split('=', 1)
            cookie[key] = value
        cookiejar = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
        session.cookies = cookiejar
        params = {
            'type': 2,
            'query': query,

        }
        while True:
            session.get("https://weixin.sogou.com/weixin", headers=self.header, params=params)
            print(session.cookies)
            session.cookies.set('SNUID', 'aaa')
            print(session.cookies)
            #pickle.dumps()
"""    
    def cookie_test(self,ip_proxy):
        if ip_proxy is not None:
            result = session.get("https://weixin.sogou.com/weixin", headers=header, params=params, cookies=cookie)
            print(result.status_code)
            if result.status_code == 200 and '需要您协助验证' not in result.text:
                print(session.cookies)
                #测试是否为登录状态
                html_page12 = session.get("https://weixin.sogou.com/weixin?oq=&query=NBA&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=2&_sug_=n&type=2&sst0=1578919427637&page=12&ie=utf8&p=40040108&dp=1&w=01015002&dr=1")
                html_page12.encoding = 'utf-8'
                print(html_page12.text)
"""
if __name__ == "__main__":
    cookie = CookiePool()
    print(cookie.get_proxy())
    print(cookie.get_cookie())