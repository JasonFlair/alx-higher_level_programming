#!/bin/bash
# displays all HTTP methods/options the server will accept.
curl -sIX OPTIONS "$1" | grep "Allow" | cut -b 8-
