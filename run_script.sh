#!/bin/bash

# Array of Python scripts to execute
scripts=(
    "FIMReport.py"
    "GDPRReport.py"
    "HIPAAReport.py"
    "malwareReport.py"
    "MitreAttackReport.py"
    "NISTReport.py"
    "PCIDSSReport.py"
    "threatHuntingReport.py"
    "TSCReport.py"
    "VirusTotalReport.py"
)

# Loop indefinitely
while true
do
    for script in "${scripts[@]}"
    do
        echo "Running script: $script"
        python3 "$script"
        echo "Script $script completed."
    done

    echo "All scripts completed. Waiting for 30 minutes..."
    sleep 1800  # Sleep for 30 minutes (1800 seconds)
done
