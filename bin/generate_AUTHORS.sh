#!/bin/bash
test -z "$PROJECT_DIRECTORY" && . "$(dirname "$0")"/lib/environment_up.sh
AUTHORS_FILE="$PROJECT_DIRECTORY/AUTHORS"
echo "# Generated by $0" > "$AUTHORS_FILE"
echo "Commits Author" >> "$AUTHORS_FILE"
git shortlog -s -e -n | sed 's/@/ AT /g' | sed 's/\./ DOT /g' >> "$AUTHORS_FILE"
