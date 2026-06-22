# Establish current directory location context
$PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $PSScriptRoot

$VenvDir = ".venv" # Changed from "venv" to match your existing folder
$RequirementsFile = "requirements.txt"

# Step 1: Create the virtual environment if missing
if (-not (Test-Path -Path $VenvDir)) {
    Write-Host "Creating Python Virtual Environment (.venv)..."
    python -m venv $VenvDir
    if (-not $?) {
        Write-Error "Failed to create virtual environment. Verify Python is installed."
        Exit
    }
}

# Step 2: Establish system control execution paths
$ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
$PipExe = Join-Path $VenvDir "Scripts\pip.exe"
$StreamlitExe = Join-Path $VenvDir "Scripts\streamlit.exe"

# Step 3: Check and resolve dependency frameworks
if (Test-Path -Path $RequirementsFile) {
    Write-Host "Verifying and installing dependencies..."
    & $PipExe install -r $RequirementsFile --quiet
} else {
    Write-Host "Warning: requirements.txt not found. Skipping dependency resolution."
}

# Step 4: Final verification check
if (-not (Test-Path -Path $StreamlitExe)) {
    Write-Error "Streamlit binary missing inside environment framework."
    Exit
}

# Step 5: Activate and launch global network server access paths
Write-Host "Launching Local AI Web Server across your network..."
& $ActivateScript
& $StreamlitExe run app.py --server.address 0.0.0.0