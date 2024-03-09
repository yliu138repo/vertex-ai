#!/bin/bash
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-H ": crested-sunup-415409" \
https://vision.googleapis.com/v1/images:annotate -d @vision-request.json

# export GOOGLE_APPLICATION_CREDENTIALS="crested-X-Goog-User-Projectsunup-415409-954d16add813.json"

# gcloud auth application-default print-access-token