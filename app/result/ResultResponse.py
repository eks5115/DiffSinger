from fastapi.responses import JSONResponse


class ResultResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        response_data = {
            'code': self.status_code,
            'message': 'success' if self.status_code == 200 else 'error',
            'data': content
        }
        return super().render(response_data)
