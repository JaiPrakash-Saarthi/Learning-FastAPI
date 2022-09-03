from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def inndex():
    return {'Hello':{'name':'Jai Prakash'}}



