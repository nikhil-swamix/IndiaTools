import sys
import os


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
					mx.cleanup()
				except Exception as e:
					...
		pass


def fetch_latest_copy():
	progressive_import()
	# print((mx.get_page('https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text))
	mx.fwrite('modulexnew.py', mx.get_page(
            'https://raw.githubusercontent.com/BinarySwami-10/modulex/master/modulex.py').text
           )


fetch_latest_copy()
if __name__ == '__main__':
	fetch_latest_copy()
