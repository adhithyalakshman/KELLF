from fastapi import FastAPI


# main app
app=FastAPI()
@app.get("/")
def home():
    return {"message":"you are welcome"}