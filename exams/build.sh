#!/usr/bin/env bash
# Regenerate the quiz HTML for the exam folders.
#
# Usage:
#   ./build.sh                     # DEFAULT: one combined HTML for ALL folders
#   ./build.sh --single-output     # same as default (explicit)
#   ./build.sh --per-folder        # one HTML per folder (into each folder)
#   ./build.sh 1.medium            # per-folder build of just 1.medium
#   ./build.sh --single-output 1.medium 2.harder   # combine only these
#
# The default writes one self-contained exam-test-aggregate.html into the
# exams/ directory, embedding every exam from all folders.

set -euo pipefail
cd "$(dirname "$0")"

python3 build.py "$@"
