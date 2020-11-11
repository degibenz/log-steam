import asyncio
import logging
from itertools import chain

from aiohttp import web

from config import (
    SERVER_PORT,
    SERVER_HOST
)

from routers import routes

from db import (
    setup_mongo,
    close_mongo,
)

logger = logging.getLogger(__name__)


def init() -> web.Application:
    """

    :return:
    """
    app: web.Application = web.Application()

    for route in chain(*routes):
        app.router.add_route(*route)

    app.on_startup.append(setup_mongo)
    app.on_cleanup.append(close_mongo)
    return app


def main():
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    web.run_app(
        application,
        host=SERVER_HOST,
        port=SERVER_PORT
    )


logging.info("STARTING APPLICATION")
application = init()
logging.info("APPLICATION STARTED")

if __name__ == '__main__':
    main()
