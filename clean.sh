#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")" # Executes from the directory containing the script
set -e # Exit on error

echo "Cleaning build artifacts..."

# Remove build directories
rm -rf build/ mod/ lib/ src/*.f src/*.f90 bin/*.exe

echo "Clean complete."
