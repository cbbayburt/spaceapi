#!/bin/sh

# Get the 1st argument as the API endpoint
CMD=$1
shift

# Get the server URL from $SPACECMD_SERVER or fallback to localhost
SERVER=${SPACECMD_SERVER:-localhost}

# Concatenate rest of the arguments to a comma-separated list
# spacecmd expects API arguments in this format
ARGS=$(IFS=, ; printf '%s' "$*")

spacecmd --nossl -s $SERVER "api${@:+ -A $ARGS} $CMD"
