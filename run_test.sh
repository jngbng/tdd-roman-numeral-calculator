#!/usr/bin/env bash

exec watchexec -w src -w tests --clear --restart -- pytest -s --maxfail=1
