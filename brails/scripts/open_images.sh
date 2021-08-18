#!/usr/bin/bash
cut -f 1 | while read -r line; do echo _images/**/$line; done | sxiv -

