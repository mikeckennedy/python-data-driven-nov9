import pyramid.httpexceptions
from pyramid.renderers import get_renderer


class BaseController:
    def __init__(self, request):
        self.request = request
        self.layout = None
        self.setup_layout()
        self.data = self.build_merged_dicts()

    def setup_layout(self):
        layout_renderer = get_renderer(
            'the_blog:templates/shared/_layout.pt')
        impl = layout_renderer.implementation()
        self.layout = impl.macros['layout']

    def redirect(self, url, permanent=False):
        if not permanent:
            raise pyramid.httpexceptions.HTTPFound(url)

        raise pyramid.httpexceptions.HTTPMovedPermanently(url)

    def build_merged_dicts(self):
        merged = dict()
        merged.update(self.request.GET)
        merged.update(self.request.POST)
        merged.update(self.request.matchdict)

        return merged
