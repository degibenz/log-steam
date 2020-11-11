import asyncio
from aiohttp import web
import motor.motor_asyncio as aiomotor

from motor.motor_asyncio import AsyncIOMotorDatabase

from config import (
    MONGODB_CONNECTION_URL,
    MONGODB_DB_NAME,
)

__all__ = (
    'init_mongo',
    'setup_mongo',
    'close_mongo',
)


async def init_mongo() -> aiomotor.AsyncIOMotorClient:
    """

    :return:
    """
    loop = asyncio.get_event_loop()
    client = aiomotor.AsyncIOMotorClient(MONGODB_CONNECTION_URL, io_loop=loop)
    return client[MONGODB_DB_NAME]


async def setup_mongo(app: web.Application) -> AsyncIOMotorDatabase:
    """

    :param app:
    :return:
    """
    db = await init_mongo()
    app['db'] = db
    return db


async def close_mongo(app):
    """

    :param app:
    :return:
    """
    db = app['db']
    db.client.close()
