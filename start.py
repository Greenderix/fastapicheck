import uvicorn

from src import create_app

if __name__ == '__main__':
    uvicorn.run(app=create_app(), port=5050)