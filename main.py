import json

if __name__=="__main__":
    with open('./config.json') as j:
        res = json.load(j)
        for l in res:
            