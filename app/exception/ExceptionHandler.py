from fastapi import Request
from fastapi.responses import JSONResponse


class ExceptionHandler:
    async def __call__(self, request: Request, e: Exception):
        return JSONResponse(
            status_code=200,
            content={
                'code': 500,
                'message': str(e)
            },
        )
