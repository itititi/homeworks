import aiohttp
from aiohttp import web

async def create_ad(request):
    data = await request.json()
    # логика создания объявления

async def get_ad(request):
    ad_id = request.match_info['id']
     # логика получения объявления по id

async def delete_ad(request):
   ad_id = request.match_info['id']
   # логика удаления объявления по id

app = web.Application()
app.router.add_post('/ads', create_ad)
app.router.add_get('/ads/{id}', get_ad)
app.router.add_delete('/ads/{id}', delete_ad)

web.run_app(app)