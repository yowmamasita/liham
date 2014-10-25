# -*- coding: utf-8 -*-
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
    def api_get(self, key):
        obj = Object.get(key)
        if not obj:
            return 404
        self.meta.change_view('json')
        self.context['data'] = json.loads(obj.content)

    @route_with('/<key>', methods=['POST'])
    def api_store(self, key):
        if Object.get(key):
            return 405
        if self.request.content_type == 'application/json':
            content = json.loads(self.request.body)
        else:
            content = json.dumps({k: v for k, v in self.request.params.items()})
        Object.create(key, content)
        return 200
