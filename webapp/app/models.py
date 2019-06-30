from pymodm import MongoModel, fields, EmbeddedMongoModel


class User(EmbeddedMongoModel):
    user_id=fields.CharField()
    user_refresh_token=fields.CharField()
    user_emails=fields.ListField()
    phone_numbers=fields.ListField()
    legal_names=fields.ListField()
    node_id=fields.CharField()

class Mercury(MongoModel):
    users=fields.EmbeddedDocumentListField(User)
