#!/usr/bin/env bash

set -eu

base_dir=$(dirname "$0")

source "${base_dir}/../../setting.sh"

"$base_dir"/fetch.sh
"$base_dir"/tweet.sh

