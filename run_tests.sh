#!/usr/bin/env bash
if [[ $# -eq 0 ]]; then
    pytest -s --failed-first
else
    pytest -s --failed-first --cmdopt "$@"
fi
