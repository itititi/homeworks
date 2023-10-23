import datetime
import aiohttp_jinja2


async def create_advertisement(request):
    data = await request.json()

    # логика создания объявления


async def get_advertisement(request):
    ad_id = int(request.match_info['id'])

    # логика получения объявления по id


async def delete_advertisement(request):
    ad_id = int(request.match_info['id'])

    # логика удаления объявления по id


aiohttp_jinja2.template('index.html')


async def index_page():
    return {}