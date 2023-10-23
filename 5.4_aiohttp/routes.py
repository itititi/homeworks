import aiohttp_jinja2
import jinja2

from views import create_advertisement, get_advertisement, delete_advertisement


def setup_routes(app):
    app.router.add_post('/advertisement', create_advertisement)
    app.router.add_get('/advertisement/{id}', get_advertisement)
    app.router.add_delete('/advertisement/{id}', delete_advertisement)

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('ad', 'templates')
    )