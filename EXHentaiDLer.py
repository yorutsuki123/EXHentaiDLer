# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:09:05 2020

@author: Yorutsuki
"""

import os
import requests
from bs4 import BeautifulSoup

class Error(Exception):
    pass

class UserCookieError(Error):
    pass

class UrlError(Error):
    pass

class User:
    def __init__(self, ipb_member_id='5292377', ipb_pass_hash='5f873f7113d581c5801e23dd81e30a51', igneous='220751a2c'):
        self.ipb_member_id = ipb_member_id
        self.ipb_pass_hash = ipb_pass_hash
        self.igneous = igneous
        if not self.testAccount():
            raise UserCookieError
        print('Login Success')
    
    def getHeaders(self) -> dict:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 
            'Cookie': 'igneous=%s; ipb_member_id=%s; ipb_pass_hash=%s' % (self.igneous, self.ipb_member_id, self.ipb_pass_hash)
        }
        return headers
    
    def testAccount(self) -> bool:
        url = 'https://exhentai.org/'
        r = requests.get(url, headers=self.getHeaders())
        return int(r.headers['Content-length']) != 0

class ExHentai:
    def __init__(self, user: User, url='https://exhentai.org/g/1707640/a56d9463e2/'):
        self.user = user
        self.pg_list = []
        self.title = ''
        (p1, p2) = ('', '')
        lst = url.split('/')
        for i in lst:
            if len(i) == 7:
                p1 = i
            if len(i) == 10:
                p2 = i
        if len(p1) != 7 or len(p2) != 10:
            raise UrlError
        self.url = 'https://exhentai.org/g/%s/%s/' % (p1, p2)
        if not self.testUrl():
            raise UrlError
        print('Get Data Success:', self.title, 'Pages:', len(self.pg_list))
    
    def testUrl(self) -> bool:
        r = requests.get(self.url, headers=self.user.getHeaders())
        soup = BeautifulSoup(r.text, 'html.parser')
        lst = soup.select('#gdt .gdtm')
        if len(lst) == 0:
            return False
        for i in lst:
            self.pg_list.append(i.find('a')['href'])
        #print(self.pg_list)
        self.title = soup.select_one('h1#gn').string
        for i in '/\\:<>?*|"':
            self.title = self.title.replace(i, ' ')
        return True
    
    def download(self, path='./') -> int:
        path = path + self.title
        if not os.path.isdir(path):
            os.mkdir(path)
        print('path:', path)
        for n, i in enumerate(self.pg_list, start=1):
            self.downloadPage(path, i, n, len(self.pg_list))
        return len(self.pg_list)
        
    def downloadPage(self, path: str, url: str, n: int, total: int):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 
        }
        r = requests.get(url, headers=self.user.getHeaders())
        soup = BeautifulSoup(r.text, 'html.parser')
        img_url = soup.select_one('img#img')['src']
        file_name = img_url.split('/')[-1]
        with open(path + '/' + file_name, 'wb') as f:
            print('(%d/%d)' % (n, total), 'downloading', path + '/' + file_name)
            f.write(requests.get(img_url, headers=headers).content)
        print('downloaded success')

def getCookies():
    ipb_member_id = ''
    ipb_pass_hash = ''
    igneous = ''
    change_cookies = False
    with open('userdata.txt', 'a') as f:
        pass
    with open('userdata.txt', 'r') as f:
        txts = f.readlines()
        if len(txts) < 3:
            print('No cookies yet, please input them.')
            change_cookies = True
        else:
            ipb_member_id = txts[0].replace('\n', '')
            ipb_pass_hash = txts[1].replace('\n', '')
            igneous = txts[2].replace('\n', '')
            print('Your cookies:')
            print('ipb_member_id:', ipb_member_id)
            print('ipb_pass_hash:', ipb_pass_hash)
            print('igneous:', igneous)
            ans = input('Do you want to change them(Y/N)?')
            if 'Y' in ans or 'y' in ans:
                change_cookies = True
    if change_cookies:
        return changeCookies()
    return (ipb_member_id, ipb_pass_hash, igneous)
    
def changeCookies() -> set:
    ipb_member_id = input('ipb_member_id: ')
    ipb_pass_hash = input('ipb_pass_hash: ')
    igneous = input('igneous: ')
    return (ipb_member_id, ipb_pass_hash, igneous)

def createUser(cookies: set) -> User:
    try:
        user = User(cookies[0], cookies[1], cookies[2])
    except UserCookieError:
        print('Your cookies are wrong, please input again.')
        cookies = changeCookies()
        return createUser(cookies)
    with open('userdata.txt', 'w') as f:
        f.writelines([cookies[0] + '\n', cookies[1] + '\n', cookies[2] + '\n'])
    return user

def getExUrl(user: User) -> ExHentai:
    try:
        ex_pg = ExHentai(user, input('ExHentai URL:'))
    except UrlError:
        print('Your URL is wrong, please input again.')
        return getExUrl(user)
    return ex_pg

def main():
    user = createUser(getCookies())
    print('Input your folder path, start from "./"(local) or "C:/"(global) etc.')
    path = input('Path: ')
    again = True
    while again:
        ex_pg = getExUrl(user)
        ex_pg.download(path)
        print('Done.')
        ans = input('Continue(Y/N)?')
        if 'N' in ans or 'n' in ans:
            again = False

if __name__ == '__main__':
    main()