from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn
app=FastAPI()

@app.get("/home")
def home():
    return "this is home"
@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")
if __name__ == "__main__":
    uvicorn.run(app, debug=True)