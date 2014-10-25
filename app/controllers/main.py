from ferris import Controller, messages, route_with
from app.models.object import Object
import json


class Main(Controller):
    class Meta:
        prefixes = ('api',)
        components = (messages.Messaging,)
        Model = Object

    @route_with('/')
    def index(self):
        pass

    @route_with('/<key>', methods=['GET'])
    def get(self, key):
        return json.loads(Object.get(key).content)

    @route_with('/<key>', methods=['POST', 'PUT'])
    def store(self, key):
        if self.request.content_type == 'application/json':
            content = json.loads(self.request.body)
        else:
            content = json.dumps(self.request.params)
        Object.create(key, content)
        return 200
