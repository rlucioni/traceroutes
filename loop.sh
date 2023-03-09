#!/usr/bin/env bash
set -e

INPUT='hosts.txt'
OUTPUT='data.txt'

while true
do
    while read -r line
    do
      date -Iseconds >> $OUTPUT
      traceroute -q 1 -z 500 -m 16 -w 2 $line >> $OUTPUT

      echo "ok"

      sleep 3
    done < $INPUT
done
