from flask_restplus import Namespace, fields


class RecordDto:
    api = Namespace('record', description='record related operations')
    record = api.model('record', {
        'device_ip': fields.String(required=True, description='record device ip'),
        'value': fields.String(required=True, description='record value')
    })