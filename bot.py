from config import keys
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def order(k):
    # driver.get('https://www.supremenewyork.com/shop/shirts/r9ftji7km')
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k['address'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['postcode'])
    driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(k['card_number'])
    driver.find_element_by_xpath('//*[@id="vval"]').send_keys(k['card_cvv'])

    #state
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[7]').click()

    #day
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k["card_exp_mo"])).click()

    #year
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k["card_exp_yr"])).click()

    #Terms and conditions
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

    #process payment
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()

    
if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    order(keys)
