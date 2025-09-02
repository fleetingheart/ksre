#/bin/sh

VERSION="v0.0.0-unknown"
RE='[^0-9]*\([0-9]*\)[.]\([0-9]*\)[.]\([0-9]*\)\([0-9A-Za-z-]*\)'

if [ -z "${CI_COMMIT_TAG}"]; then
    PREVIOUS_TAG=`git -c 'versionsort.suffix=-' \
                    ls-remote --exit-code --refs --tags \
                    'https://codeberg.org/fhs/katawa-shoujo-re-engineered.git' \
                    'v*.*.*' | sort -k2 -V | tail -n 1 | cut -d '/' -f 3`
    MAJOR=`echo $PREVIOUS_TAG | sed -e "s#$RE#\1#"`
    MINOR=`echo $PREVIOUS_TAG | sed -e "s#$RE#\2#"`
    PATCH=`echo $PREVIOUS_TAG | sed -e "s#$RE#\3#"`
    let PATCH+=1
    VERSION="v${MAJOR}.${MINOR}.${PATCH}-${CI_PIPELINE_CREATED}-${CI_COMMIT_SHA:0:10}"
    GAME_VERSION="${MAJOR}.${MINOR}.${PATCH}-${CI_COMMIT_SHA:0:4}"
else
    VERSION="${CI_COMMIT_TAG}"
    GAME_VERSION="${CI_COMMIT_TAG%%v}"
fi

echo "CI_PRETTY_VERSION=${VERSION}" | tee -a .env
echo "CI_KSRE_VERSION=${GAME_VERSION}" | tee -a .env
