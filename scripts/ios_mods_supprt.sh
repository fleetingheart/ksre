#!/bin/sh
set -e

P="$1"

if [ -d "$P" ]; then
    P="$P/Info.plist"
fi

if [ -z "$P" ] || [ ! -f "$P" ]; then
    echo "usage: $0 /path/to/ksre-xcode" >&2
    exit 1
fi

/usr/libexec/PlistBuddy -c 'Add :UIFileSharingEnabled bool true' "$P" 2>/dev/null || \
/usr/libexec/PlistBuddy -c 'Set :UIFileSharingEnabled true' "$P"

/usr/libexec/PlistBuddy -c 'Add :LSSupportsOpeningDocumentsInPlace bool true' "$P" 2>/dev/null || \
/usr/libexec/PlistBuddy -c 'Set :LSSupportsOpeningDocumentsInPlace true' "$P"
