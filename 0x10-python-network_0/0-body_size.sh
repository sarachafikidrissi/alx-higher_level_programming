#!/bin/bash
#get the size off a url body
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
