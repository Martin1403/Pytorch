TTS Pytorch CPU
===============

<video controls width="250">
 <source src="samples/test.mp4"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>

### python3.9
```
python -m venv .venv && \
source .venv/bin/activate && \
pip install -U pip && \
pip install -r requirements.txt
pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```
### apt
```
apt-get -y install libopenblas-base libgomp1 libatomic1
```
### voices:
```
apt-get install p7zip-full
7za x voices/archive/voices.7z.001 -ovoices/
```
### Run:
###### /

```
python main.py \
    -t "Hello, how are you today?" \
    -n "kathleen-glow_tts" \
    -q "high" \
    -s "samples/test.wav"
```

**Note:**

Simple multilanguage TTS.

### [Links:]()
+ ###### [Larynx](https://github.com/rhasspy/larynx) tts GitHub, download voices
