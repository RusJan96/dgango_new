from litestar import Literstar, get, Request

@get('/hello')
async def hello_message(request:Request) -> str:
    return "Привет пользователь"


app = Litestar(
    route_handlers=[hello_message]
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)