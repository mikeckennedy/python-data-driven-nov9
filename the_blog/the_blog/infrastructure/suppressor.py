import pyramid_handlers


class suppress(pyramid_handlers.action):
    def __init__(self, **kw):
        kw['request_method'] = 'NOT_A_HTTP_VERB'
        super().__init__(**kw)
