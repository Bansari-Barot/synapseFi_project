from pymodm import MongoModel, fields, EmbeddedMongoModel


class UserInfo(EmbeddedMongoModel):
    user_id=fields.CharField()
    user_refresh_token=fields.CharField()
    logins=fields.ListField()
    phone_numbers=fields.ListField()
    node_id=fields.ListField()

class Mercury(MongoModel):
    users=fields.EmbeddedDocumentListField(UserInfo)
