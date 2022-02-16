import sys
import os
from datetime import datetime

try:
    import requests
except Exception as e:
    os.system('pip install requests')

VERSION_LOCK = 1


def progressive_import():
    global mx
    success = 0
    importlevel = "./"
    try:
        import modulex as mx
        print("mx imported")
    except Exception as e:
        for i in range(4):
            if not success:
                try:
                    sys.path.append(importlevel)
                    from modulex import modulex as mx
                    success = 1
                    print("mx imported")
                except Exception as e:
                    pass


def fetch_latest_copy():
    # print((mx.get_page('https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text))
    if not os.path.exists('modulex.py'):
        pagedata = requests.get(
            'https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text
        print('page fetched, now writing')
        open('modulex.py', '+w', encoding="utf-8").write(f"#last fetched on {datetime.now()}\n" + pagedata, )
    else:
        print('Modulex already present')



if __name__ == '__main__':
    print(datetime.now())
    fetch_latest_copy()
else:
    sys.path.append('../')
    try:
        import modulex as mx
    except:
        sys.path.append('../../')
        import modulex as mx
