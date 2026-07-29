param(
    [ValidateSet('all', 'cursor', 'copilot', 'claude')]
    [string]$Target = 'all'
)

$ErrorActionPreference = 'Stop'
python (Join-Path $PSScriptRoot 'generate_agent_rules.py') --target $Target
python (Join-Path $PSScriptRoot 'validate_agent_support.py')
Write-Output "Agent support installed for: $Target"
