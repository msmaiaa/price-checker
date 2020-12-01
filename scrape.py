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
    else:
        nome = driver.find_element_by_xpath(nameXpathAv)
        price = driver.find_element_by_xpath(priceXpath).text
        nicePrint(loja, nome, True, price)
        
    driver.close()


def nicePrint(loja, nome, available, price=""):
    if not available:
        print(Fore.CYAN + f'[{loja}]' + Fore.WHITE + f'[{nome.text}]' + Fore.RED + ' SEM ESTOQUE')
    else:
        print(Fore.CYAN + f'[{loja}]' + Fore.GREEN + f'[{nome.text}]' + Fore.MAGENTA + f' {price}')

#if __name__ == '__main__':
    #print(Fore.RED + 'some red text')
