#!/usr/bin/env bash
word=$(xsel -o | tr '[:upper:]' '[:lower:]')
path=$(dirname "$(readlink -f "$0")")
result=$($path/translate.py $word)
notify-send --icon=info "[ $word ]" "$(echo $result)"
