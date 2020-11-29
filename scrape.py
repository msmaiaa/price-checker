from colorama import init
init()
from colorama import Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

def start(loja, url, naXpath, priceXpath, nameXpathUn, nameXpathAv):
    driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')  
    driver.get(url)
    time.sleep(2)
    notAvailable = driver.find_elements_by_xpath(naXpath)
    if len(notAvailable) >= 1:
        nome = driver.find_element_by_xpath(nameXpathUn)
        nicePrint(loja, nome, False)
        driver.quit()
    else:
        time.sleep(60)
        nome = driver.find_element_by_xpath(nameXpathAv)
        price = driver.find_element_by_xpath(priceXpath)
        nicePrint(loja, nome, price, True)
        driver.quit()
    

def nicePrint(loja, nome, available, price=False):
    if not available:
        print(Fore.CYAN + f'[{loja}]' + Fore.WHITE + f'[{nome.text}]' + Fore.RED + ' SEM ESTOQUE')
    else:
        print(Back.GREEN + Fore.CYAN + f'[{loja}]' + Fore.WHITE + f'[{nome.text}]' + Fore.BLACK + f' [{price}]')

#if __name__ == '__main__':
    #print(Fore.RED + 'some red text')
