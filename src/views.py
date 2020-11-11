import json
from aiohttp import web

from http import HTTPStatus

from bson.json_util import dumps

from config import MONGODB_DB_NAME


class ApiWithDB(web.View):

    async def get(self) -> web.Response:
        """

        :return:
        """
        db = self.request.app['db']

        try:
            page_num: int = int(self.request.query.get('page', '1'))
            if page_num <= 0:
                page_num = 1
        except(TypeError, ValueError):
            page_num = 1

        page_size: int = 50
        skip_items: int = page_size * (page_num - 1)

        logs_items = await db[MONGODB_DB_NAME].find().skip(skip_items) \
            .limit(page_size).to_list(None)

        return web.json_response(
            data=json.loads(dumps(logs_items)), status=HTTPStatus.OK
        )
