#!/usr/bin/env bash
cd "alfheimproject/conf"
for file in *.example.json;
do
    mv "$file" "${file/.example.json/.json}"
done