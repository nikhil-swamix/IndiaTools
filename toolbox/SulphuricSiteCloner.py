import modulex as mx

soup = mx.make_soup(mx.fread('homepage.html'))


def gather_css():
    mx.touch('css/')
    SUPER_CSS = ''
    for l in soup.select('link'):
        url = l['href']

        if url.startswith('//'):
            url = 'http:' + url

        if 'css' in url:
            SUPER_CSS += mx.get_page(url).text
            print(url)

    mx.fwrite('css/style.css', SUPER_CSS)


def gather_js():
    mx.touch('js/')
    SUPER_JS = ''
    for l in soup.select('script'):
        url = l.get('src')
        if not url:
            continue

        if url.startswith('//'):
            url = 'http:' + url

        if 'js' in url:
            SUPER_JS += mx.get_page(url).text
            print(url)

    mx.fwrite('js/main.js', SUPER_JS)

def gather_images():
    mx.touch('img/')
    print(len(soup.select('img')))
    for i in soup.select('img'):
        url=i['src']
        ext=url.split('.')[-1]
        url_hash=mx.hash(url)
        dl_fn = lambda: open(f'./img/{url_hash}.{ext}', 'wb').write(mx.get_page(url).content)
        # mx.apply_async(dl_fn)
        dl_fn()
        
        # print(i['src'])

def transform_imgurl():
    for i in soup.select('img'):
        url=i['src']
        ext=url.split('.')[-1]
        url_hash=mx.hash(url)

        orignal = i['src']
        i['src'] = f'./img/{url_hash}.{ext}'
        i['src-orignal']=orignal

    # print(soup.select('img'))

if __name__ == '__main__':
    # gather_css()
    # gather_js()   
    gather_images()
    # transform_imgurl()
    print(soup)