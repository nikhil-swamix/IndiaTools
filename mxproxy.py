import sys


def progressive_import():
    success = 0
    importlevel = "./"
    try:
        import modulex as mx
    except Exception as e:
        for i in range(4):
            if not success:
                try:
                    sys.path.append(importlevel)
                    from modulex import modulex as mx
                    success = 1
                    print("mx imported")
                    mx.cleanup()
                except Exception as e:
                    ...
        pass

def fetch_latest_copy():
    progressive_import()
    mx.get_page()

if __name__ != '__main__':
	fetch_latest_copy()

