import datetime

from app.main import db
from app.main.model.record import Record


def save_new_record(data):

    new_record = Record(
        device_ip=data['device_ip'],
        generation_time=datetime.datetime.utcnow(),
        value=data['value']
    )
    save_changes(new_record)
    response_object = {
        'status': 'success',
        'message': 'Successfully added record to database.'
    }
    return response_object, 201


def get_all_records():
    return Record.query.all()


def get_records_by_ip(device_ip):
    return Record.query.filter_by(device_ip=device_ip).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()