from ferris import BasicModel, ndb


class Object(BasicModel):

    name = ndb.StringProperty()
    content = ndb.JsonProperty()

    @classmethod
    def create(cls, k, v):
        cls(id=k, name=k, content=v).put()

    @classmethod
    def get(cls, k, v):
        return ndb.Key(cls, k).get()
