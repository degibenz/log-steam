import logging

from typing import Dict

import json
from json import JSONDecodeError

import asyncio
import aiohttp

from aiohttp.client_exceptions import ClientConnectionError
import motor.motor_asyncio as aiomotor

from db import init_mongo

from schemas import MessageFromVehicle

from config import (
    VEHICLE_CONNECTION_URL,
    MONGODB_DB_NAME,
)

logger = logging.getLogger(__name__)


async def vehicle_ws_client():
    session = aiohttp.ClientSession()

    try:
        async with session.ws_connect(VEHICLE_CONNECTION_URL, ) as ws:
            await ws_client(ws, )
    except(ClientConnectionError,) as err:
        logger.error(err)


async def ws_client(ws):
    db = await init_mongo()

    async for msg in ws:
        future: asyncio.Future = asyncio.Future()
        future.set_result(msg.data)
        asyncio.ensure_future(insert_log_record(future, db))


async def insert_log_record(
        future: asyncio.Future, connect: aiomotor.AsyncIOMotorClient
):
    msg = future.result()
    data_from_ws: Dict[str:str] = None

    try:
        data_from_ws = json.loads(msg)
    except(JSONDecodeError,) as err:
        logger.error("Incorrect payload :: %s" % err)

    if data_from_ws:
        data, error = MessageFromVehicle().load(data_from_ws)

        if not error:
            try:
                await connect[MONGODB_DB_NAME].insert_one(data)
            except(Exception,) as err:
                logger.error(err)
        else:
            logger.error(error)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(vehicle_ws_client())
