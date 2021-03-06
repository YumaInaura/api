#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")
source "${base_dir}/../../setting.sh"

mkdir -p "$log_dir"
rm -rf "$log_dir"/*

eval "$base_dir"/fetch-all.sh
eval "$base_dir"/preview.sh
eval "$base_dir"/translate-all.sh
eval "$base_dir"/create-seed.sh
eval "$base_dir"/create-all.sh

