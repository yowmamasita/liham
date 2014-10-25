from ferris import BasicModel, ndb
import binascii


class Object(BasicModel):

    name = ndb.StringProperty()
    content = ndb.JsonProperty()

    @classmethod
    def create(cls, k, v):
        cls(id=binascii.crc32(k), name=k, content=v).put()

    @classmethod
    def get(cls, k):
        return ndb.Key(cls, binascii.crc32(k)).get()
