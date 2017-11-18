#!/usr/bin/env bash

prefix="/usr/local"

mkdir -p $prefix/bin
rm -rf $prefix/bin/xcw*

pushd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null
  for g in git*; do
    install $g "$prefix/bin/$g"
  done
popd > /dev/null

PATH+=:$prefix/bin
git lfs install
