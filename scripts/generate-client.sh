#! /bin/bash

npx @openapitools/openapi-generator-cli version-manager set 6.2.1
npx -q @openapitools/openapi-generator-cli generate -i schemas/docs.yaml -g python -c schemas/config.json