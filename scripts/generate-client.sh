#! /bin/bash

pip install openapi-python-client
rm -rf coffee-freaks-api-client
openapi-python-client generate --path schemas/docs.yaml --config schemas/config.yaml