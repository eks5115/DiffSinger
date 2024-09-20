from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class ResponseAdviceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response
