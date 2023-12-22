from fastapi import FastAPI

import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"food": "Pasty",
            "cost": 1.20}

if __name__ == "__main__":
    uvicorn.run(app)