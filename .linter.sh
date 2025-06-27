#!/bin/bash
cd /home/kavia/workspace/code-generation/eventease-api-61547-bc414e31/event_manager_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

