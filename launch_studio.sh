#!/usr/bin/env bash

# (/bin/obs-studio > /dev/null 2> /dev/null &)
(/usr/bin/obs > /dev/null 2> /dev/null &)
(code .&)
(code ~/Dropbox/share/log/&)
xdg-open ~/auravenphoenix_justice/attaque 
# xdg-open ~/auravenphoenix_justice/defense 
xdg-open ~/studio 
