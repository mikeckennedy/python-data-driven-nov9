from pyramid.renderers import get_renderer


class BaseController:
    def __init__(self, request):
        self.request = request
        self.layout = None
        self.setup_layout()

    def setup_layout(self):
        layout_renderer = get_renderer(
            'the_blog:templates/shared/_layout.pt')
        impl = layout_renderer.implementation()
        self.layout = impl.macros['layout']

