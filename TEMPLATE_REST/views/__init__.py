from pyramid.renderers import JSON
from datetime import datetime


def includeme(config):
    settings = config.get_settings()
    json_renderer = JSON()
    def datetime_adapter(obj, request):
        return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    json_renderer.add_adapter(datetime, datetime_adapter)
    config.add_renderer('json', json_renderer)

    config.add_request_method(callable=lambda x: {},
                              name='validated', reify=True)
