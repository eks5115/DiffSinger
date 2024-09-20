import uvicorn
from fastapi import FastAPI
from utils.hparams import hparams
from app.model import DiffSingerForm
from app.exception import ExceptionHandler
from app.middleware import ResponseAdviceMiddleware
from app.result import ResultResponse
from app.service import infer_once

app = FastAPI()
app.add_exception_handler(Exception, ExceptionHandler())
app.add_middleware(ResponseAdviceMiddleware)


@app.post('/infer', response_class=ResultResponse)
def infer(form: DiffSingerForm):
    output = infer_once(form.inputs.dict())
    return {
        'pcm': output.tolist(),
        'sample_rate': hparams['audio_sample_rate']
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
