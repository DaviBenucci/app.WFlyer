#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
printf '[AVISO] verify-toolchain.sh é um alias legado. Executando validação local da toolchain do agente.\n'
exec bash "$repo_root/scripts/verify-local-agent-toolchain.sh"
