import json
import utils
import time

if __name__=="__main__":
    with open('./config.json') as j:
        res = json.load(j)
        while True:
            for loja in res:
                utils.filter(loja["titulo"], loja["urls"])
            time.sleep(60)