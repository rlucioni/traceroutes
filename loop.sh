#!/usr/bin/env bash
set -e

INPUT='hosts.txt'
OUTPUT='data.txt'

while read -r line
do
  date -Iseconds >> $OUTPUT
  traceroute -q 1 -z 500 -m 32 -w 1 $line >> $OUTPUT

  echo "ok"

  sleep 3
done < $INPUT
