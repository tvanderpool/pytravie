#!/usr/bin/env bash

hooks=(
    "applypatch-msg"
    "commit-msg"
    "fsmonitor-watchman"
    "post-update"
    "pre-applypatch"
    "post-commit"
    # "pre-commit"
    "pre-merge-commit"
    "pre-push"
    "pre-rebase"
    "pre-receive"
    "prepare-commit-msg"
    "push-to-checkout"
    "sendemail-validate"
    "update"
)

cd "$(dirname "$0")/../.git/hooks"
GITHOOKS='../../.githooks'

for hook in "${hooks[@]}"; do
    if ! [ -f "$GITHOOKS/$hook" ]; then continue; fi
    if [ -f "$hook" ]; then
        mv "$hook" "$hook.bak"
    fi
    ln -sf "$GITHOOKS/$hook" "$hook"
    # chmod +x "$GITHOOKS/$hook"
done

# Check if pre-commit command exists
if ! command -v pre-commit &> /dev/null; then
    read -p "Install pre-commit? 'pip install pre-commit'? (y/n): " install_precommit
    if [ "$install_precommit" == "y" ]; then
        pip install pre-commit
    fi
fi
if ! command -v pre-commit &> /dev/null; then
    pre-commit install
fi
