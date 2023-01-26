from starlette_context import plugins
from starlette_context.middleware import RawContextMiddleware as BaseContextMiddleware


class LogPyContextMiddleware(BaseContextMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app, plugins=(plugins.request_id.RequestIdPlugin(),))

    async def set_context(self, request) -> dict:
        return await super().set_context(request)
