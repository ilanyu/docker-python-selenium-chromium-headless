docker-python-selenium-chromium-headless

~/test/main.py

	from selenium import webdriver

	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	options.add_argument('ignore-certificate-errors')
	options.add_argument("test-type")
	options.add_argument("no-sandbox")
	options.add_argument("disable-gpu")
	options.binary_location = "/usr/bin/chromium-browser"
	browser = webdriver.Chrome(options=options)
	browser.set_page_load_timeout(120)
	browser.set_script_timeout(120)
	browser.get("http://www.baidu.com/")
	browser.close()

Generate requirements.txt file

	cd ~/test
	pip install pipreqs
	pipreqs ./

and run

	docker run -d -v ~/test:/usr/src/app ilanyu/python-selenium-chromium-headless
