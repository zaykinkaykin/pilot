import aiohttp
from aiohttp import web
from aiohttp.client import request
HOST_IP="0.0.0.0"
HOST_PORT=1724

async def skill_hello(request_obj):
    request = await request_obj.json
    response ={}
    response ["version"]=request ["version"]
    response ["session"]=request ["session"]
    response ["response"]= {"end_session": False}
    response ["response"]["text"]="hii"
    response ["response"]["end_session"]= True
    return web.json_response(response)


def init():
    app=web.Application()
    app.router.add_post("/skill_hello",skill_hello)
    web.run_app(app, host=HOST_IP , port=HOST_PORT)

   

if __name__ == "__main__" :
    init()