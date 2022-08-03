#!/bin/bash

for ((i=0;i<100;i++)); do curl -s localhost; echo; done | sed -rn 's/.* on ([a-f0-9]+)\.<.*/\1/p' | sort | uniq -c | /bin/cat -n
