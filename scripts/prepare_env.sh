#/bin/sh

VERSION="v0.0.0-unknown"

if [ -z "${CI_COMMIT_TAG}"]; then
    PREVIOUS_TAG=`git -c 'versionsort.suffix=-' \
                    ls-remote --exit-code --refs --tags \
                    'https://codeberg.org/fhs/katawa-shoujo-re-engineered.git' \
                    'v*.*.*' | sort -k2 -V | tail -n 1 | cut -d '/' -f 3`
    VERSION="${PREVIOUS_TAG}-$(date +%s)-${CI_COMMIT_SHA:0:10}"
else
    VERSION=$CI_COMMIT_TAG
fi

echo "CI_PRETTY_VERSION=${VERSION}" | tee .env
