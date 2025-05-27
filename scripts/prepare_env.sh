#/bin/sh

VERSION="v0.0.0-unknown"

if [ -z "${CI_COMMIT_TAG}"]; then
    VERSION="v0.0.0-$(date +%s)-${CI_COMMIT_SHA:0:10}"
else
    VERSION=$CI_COMMIT_TAG
fi

echo "CI_PRETTY_VERSION=${VERSION}" | tee .env
