# Vision API
## Pre-requisite
1. Create service account, and create keys
2. Download keys
3. export as global var `export GOOGLE_APPLICATION_CREDENTIALS="/d/vertex-ai/vision-api/crested-sunup-415409-954d16add813.json"`
## Python API
Install google cloud
```bash
pip install --upgrade google-api-python-client
pip install --upgrade google-cloud
pip install --upgrade google-cloud-vision
```

Export env var, so the script can detect the service account credentials
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/d/vertex-ai/vision-api/crested-sunup-415409-954d16add813.json"
```


## Reference
[Python sample](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/vision/snippets/detect/detect.py)
