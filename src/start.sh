#!/bin/bash

echo "Worker Initiated"

echo "Starting WebUI API"
python /stable-diffusion-webui/webui.py --skip-python-version-check --force-enable-xformers --precision full --no-half --skip-torch-cuda-test --ckpt /stable-diffusion-webui/models/Stable-diffusion/sd_xl_base_1.0.safetensors --lowram --opt-sdp-attention --disable-safe-unpickle --port 3000 --api --nowebui --skip-version-check  --no-hashing --no-download-sd-model &

echo "Starting RunPod Handler"
python -u /rp_handler.py
