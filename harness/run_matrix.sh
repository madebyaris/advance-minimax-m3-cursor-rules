#!/usr/bin/env bash
# Variance matrix: same buggy task, N runs with rules vs N runs bare.
# Each run starts from an identical seed; graded afterward with HIDDEN tests
# the agent never saw. Run: bash run_matrix.sh
set -u
cd "$(dirname "$0")"

SEED="seeds/calc"
PY="./.venv/bin/python"
OUT="run-matrix"
TASK="calc.py implements an integer arithmetic expression evaluator, but its test suite test_calc.py is failing. Find the root cause and fix calc.py so the whole suite passes. Run the tests to prove it. Read the contract in calc.py's docstring carefully. Do not edit the test file."

rm -rf "$OUT"; mkdir -p "$OUT"
SUMMARY="$OUT/summary.tsv"
printf "run\tarm\tfinished\tsteps\ttok_in\thidden\n" > "$SUMMARY"

run_one () {
  local name="$1" arm="$2"; shift 2
  local wd="$OUT/$name"
  mkdir -p "$wd"
  cp "$SEED/calc.py" "$SEED/test_calc.py" "$wd"/
  echo ">> running $name ($arm) ..."
  $PY agent.py "$TASK" --workdir "$PWD/$wd" --max-steps 18 "$@" > "$wd/run.log" 2>&1
  cp "$SEED/grade.py" "$wd"/
  local hidden finished steps tok
  hidden=$($PY "$wd/grade.py" 2>/dev/null | grep -o 'HIDDEN [0-9]*/[0-9]*')
  [ -z "$hidden" ] && hidden="HIDDEN err"
  finished=$(grep 'finished cleanly' "$wd/run.log" | awk -F': ' '{print $2}' | tr -d ' ')
  steps=$(grep -E '^[[:space:]]*steps' "$wd/run.log" | awk -F': ' '{print $2}' | tr -d ' ')
  tok=$(grep -E '^[[:space:]]*tokens' "$wd/run.log" | awk -F': ' '{print $2}' | awk '{print $1}')
  printf "%s\t%s\t%s\t%s\t%s\t%s\n" "$name" "$arm" "$finished" "$steps" "$tok" "$hidden" >> "$SUMMARY"
  echo ">> $name ($arm): finished=$finished steps=$steps tok_in=$tok ${hidden}"
}

for i in 1 2 3; do run_one "on-$i"  "core+craft" --rules fable5-coding-craft; done
for i in 1 2 3; do run_one "off-$i" "no-rules"   --no-rules; done

echo
echo "=== MATRIX COMPLETE ==="
column -t -s "$(printf '\t')" "$SUMMARY"
