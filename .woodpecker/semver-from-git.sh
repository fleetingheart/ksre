#!/bin/bash -eu

# This script prints out git metadata information for a given commit (or head by default)
# It assumes tags of the form `v1.2.3`, and will print prerelease versions when
# not on an exact tag.
#
# It is intended to be used like so:
#
#   cd <some-git-repo>
#   $(../semver-from-git.sh)
#
# or
#
#    $(../semver-from-git.sh <COMMIT_HASH>)
#
# For prerelease, it prints:
#
#   export GIT_BRANCH="master"
#   export GIT_SEMVER_FROM_TAG="1.0.1-master+3.ge675710"
#
# where GIT_BRANCH is the first branch it finds with the given commit, and the version string is:
# <MAJOR>.<MINOR>.<PATCH>-<BRANCH>+<COMMITS-SINCE-TAG>.<COMMIT_HASH>
#
# When on an exact tag, it prints:
#
#   export GIT_BRANCH="master"
#   export GIT_EXACT_TAG=v1.0.2
#   export GIT_SEMVER_FROM_TAG=1.0.2
#
# When the working tree is dirty, it will also put ".SNAPSHOT.<HOSTNAME>" on the end of the version
# This is useful if someone has deployed something from their local machine.

# (C) Timothy Jones, 2019, released under BSD License 2.0 (3-clause BSD license)
# https://github.com/TimothyJones 

if [ -z "${1:-}" ]; then
   COMMIT="HEAD"

   # Test whether the working tree is dirty or not
   if [ -z "$(git status -s)" ]; then
     STATUS=""
   else
     STATUS=".SNAPSHOT.$(hostname -s)"
   fi
else
   COMMIT="$1"
   STATUS="" # When looking at an exact commit, the working tree is irrelevant
fi

DESCRIBE=$(git describe --always --tags "$COMMIT")
VERSION=$(echo "$DESCRIBE" | sed 's/\(.*\)-\(.*\)-g\(.*\)/\1+\2.\3/' | sed 's/v\(.*\)/\1/')
BRANCH=$(git branch --contains "$COMMIT" | grep -e "^\*" | sed 's/^\* //')

echo "export GIT_BRANCH=$BRANCH"

EXACT_TAG=$(git describe --always --exact-match --tags "$COMMIT" 2> /dev/null || true)
if [ ! -z "$EXACT_TAG" ] ; then
  echo "export GIT_EXACT_TAG=${EXACT_TAG}"
  echo "export GIT_SEMVER_FROM_TAG=$VERSION$STATUS"
else
  # We split up the prefix and suffix so that we don't accidentally
  # give sed commands via the branch name
  PREFIX="$(echo "$VERSION" | sed 's/\(.*\)\(\+.*\)/\1/')"
  SUFFIX="$(echo "$VERSION" | sed 's/\(.*\)\(\+.*\)/\2/')"
  if [ -z $(echo "$PREFIX" | grep "-") ]; then
    echo "export GIT_SEMVER_FROM_TAG=$PREFIX-$BRANCH""$SUFFIX$STATUS"
  else
    echo "export GIT_SEMVER_FROM_TAG=$PREFIX.$BRANCH""$SUFFIX$STATUS"
  fi
fi