import sys
import os
import datetime
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
                    ...
                    pass


def fetch_latest_copy():
    progressive_import()
    # print((mx.get_page('https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text))
    if not os.path.exists('modulex.py'):
    	mx.fwrite('modulex.py', f"#last fetched on {datetime.datetime()}\n"+mx.get_page(
            'https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text
            )
    else:
    	print('Modulex already present')


fetch_latest_copy()
if __name__ == '__main__':
    fetch_latest_copy()
