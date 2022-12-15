#!/bin/bash
# sends a GET request with a header commandline option
curl -s "$1" -H "X-School-User-Id: 98"
