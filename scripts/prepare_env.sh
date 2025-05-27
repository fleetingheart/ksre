#/bin/sh

VERSION="v0.0.0-unknown"

if [ -z "${CI_COMMIT_TAG}"]; then
    VERSION="v0.0.0-${CI_COMMIT_SHA:0:10}-$(date +%s)"
else
    VERSION=$CI_COMMIT_TAG
fi

echo "VERSION=${VERSION}" | tee .env
