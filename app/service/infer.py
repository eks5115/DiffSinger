from inference.svs.ds_e2e import DiffSingerE2EInfer
from utils.hparams import set_hparams, hparams
import numpy as np

set_hparams('usr/configs/midi/e2e/opencpop/ds1000.yaml', '0831_opencpop_ds1000', print_hparams=False)
__infer = DiffSingerE2EInfer(hparams)


def __float_to_int16(floats):
    pcm_floats_clipped = np.clip(floats, -1.0, 0.999999)
    return (pcm_floats_clipped * 32768).astype(np.int16)


def infer_once(inp):
    pcm_floats = __infer.infer_once(inp)
    return __float_to_int16(pcm_floats)
