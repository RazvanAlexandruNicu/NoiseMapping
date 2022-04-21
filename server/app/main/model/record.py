from .. import db


class Record(db.Model):
    """ Record Model for storing records received from Mobile devices"""
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_ip = db.Column(db.String(255), unique=False, nullable=False)
    generation_time = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return "<Record '{}:{}:{}'>".format(self.device_ip, self.generation_time, self.value)
