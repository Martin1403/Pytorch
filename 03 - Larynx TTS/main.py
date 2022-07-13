import argparse
from concurrent.futures import ThreadPoolExecutor
import io
import os
from typing import Optional, Any, Dict

from library.lib import TTS
# from library.lib import InferenceBackend
from library.lib.wavfile import write

base = os.path.abspath(os.path.dirname(__name__))

max_thread_workers: Optional[int] = None
tts_settings: Dict[str, Any] = {"noise_scale": 0.667, "length_scale": 1.0}
voc_settings: Dict[str, Any] = {"denoiser_strength": 0.005}


def main(args):
    # backend = InferenceBackend("pytorch")
    executor = ThreadPoolExecutor(max_workers=max_thread_workers)
    tts = TTS(voice_or_lang=args.name,
              vocoder_or_quality=args.quality,
              backend="pytorch",
              tts_settings=tts_settings,
              vocoder_settings=voc_settings,
              executor=executor,
              denoiser_strength=voc_settings["denoiser_strength"],
              custom_voices_dir=f"{base}/voices/",
              )

    tts_results = tts.text_to_speech(text=args.text)
    for result_idx, result in enumerate(tts_results):
        with io.BytesIO() as wav_io:
            write(wav_io, result.sample_rate, result.audio)
            wav_data = wav_io.getvalue()
            if os.path.exists(args.save):
                os.remove(args.save)
            with open(args.save, mode='bx') as f:
                f.write(wav_data)


# DIRECTORIES
os.makedirs("samples", exist_ok=True)
os.makedirs("voices", exist_ok=True)

# SETTINGS
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', help="Text to synthesize")
parser.add_argument('-n', '--name', help="Model name")
parser.add_argument('-s', '--save', default="samples/test.wav", help="Save output")
parser.add_argument('-q', '--quality', choices=["high", "medium", "low"], help="Text to synthesize")

if __name__ == '__main__':
    try:
        main(parser.parse_args())
    except KeyboardInterrupt:
        pass
