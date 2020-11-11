from datetime import datetime

from marshmallow import (
    fields,
    Schema,
)


class MessageFromVehicle(Schema):
    component = fields.String(required=True)
    country = fields.String(required=True, default="USA")
    description = fields.String(required=True)
    model = fields.String(required=True)
    created_time = fields.DateTime(default=datetime.utcnow)
