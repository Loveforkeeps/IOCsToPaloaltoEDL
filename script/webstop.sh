#!/bin/bash
ps aux | grep "python -m SimpleHTTPServer" | awk '{print $2}' |xargs kill
