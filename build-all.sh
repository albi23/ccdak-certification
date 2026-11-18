#!/usr/bin/env bash
# Build everything: exam quiz aggregate -> study site (index.html + exam.html).
# Usage: ./build-all.sh
# Requires: python3, pip install markdown-it-py
set -euo pipefail
cd "$(dirname "$0")"

echo "==> Building exams"
python3 exams/build.py
echo "==> Building site"
python3 site/build_site.py
echo "Done: site/index.html, site/exam.html"
