from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\Downloads\chromedriver_win32\chromedriver")
driver.get('https://web.whatsapp.com/')
name = input("Enter the name of Group")
msg = input("Enter the message")
count = int(input("Enter Input"))

input("After QR code")

user = driver.find_element_by_xpath('//span[@title='+name+']')
user.click()
msg_box = driver.find_element_by_class_name("_3FeAD _1PRhq")
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()

