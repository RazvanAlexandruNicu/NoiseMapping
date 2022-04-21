from flask import request
from flask_restplus import Resource

from ..util.dto import RecordDto
from ..service.record_service import save_new_record, get_all_records, get_records_by_ip

api = RecordDto.api
_record = RecordDto.record


@api.route('/')
class RecordList(Resource):
    @api.doc('list_of_registered_records')
    @api.marshal_list_with(_record, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_records()

    @api.response(201, 'Record successfully created.')
    @api.doc('create a new record')
    @api.expect(_record, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_record(data=data)


@api.route('/<device_ip>')
@api.param('device_ip', 'The Device IP')
@api.response(404, 'Device IP not found.')
class Record(Resource):
    @api.doc('get records by ip')
    @api.marshal_list_with(_record, envelope='data')
    def get(self, device_ip):
        """get all records given their device_ip"""
        records = get_records_by_ip(device_ip)
        if not records:
            api.abort(404)
        else:
            return records
