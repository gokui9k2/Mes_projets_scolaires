#!/bin/bash

cat > requirements.txt <<EOF
aiohttp==3.9.3
aiosignal==1.3.1
annotated-types==0.6.0
anyio==4.3.0
asgiref==3.7.2
attrs==23.2.0
certifi==2024.2.2
charset-normalizer==3.3.2
dataclasses-json==0.6.4
Django==5.0.2
djangorestframework==3.14.0
frozenlist==1.4.1
greenlet==3.0.3
idna==3.6
jsonpatch==1.33
jsonpointer==2.4
marshmallow==3.21.1
multidict==6.0.5
mypy-extensions==1.0.0
mysql-connector-python==8.3.0
mysqlclient==2.2.4
numpy==1.26.4
orjson==3.9.15
packaging==23.2
pip==24.0
pydantic==2.6.4
pydantic_core==2.16.3
pysubs2==1.6.1
pytz==2024.1
PyYAML==6.0.1
requests==2.31.0
six==1.16.0
sniffio==1.3.1
SQLAlchemy==2.0.28
sqlparse==0.4.4
typing_extensions==4.10.0
typing-inspect==0.9.0
tzdata==2024.1
urllib3==2.2.1
yarl==1.9.4
EOF

mkdir -p packages

pip download -r requirements.txt -d packages

echo "Tous les paquets ont été téléchargés dans le dossier 'packages'."