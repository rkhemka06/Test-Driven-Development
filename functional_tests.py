from selenium import webdriver

browser = webdriver.Chrome('/Users/rajatkhemka/Downloads/chromedriver 2')
browser.get('http://localhost:8000')

#assert 'Django' in browser.title