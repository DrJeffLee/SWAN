#!/bin/bash
set -e # Exit on error

# Execute from the top-level SWAN directory
cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")"

echo "Cleaning build artifacts..."

# Remove build directories
rm -rf build/ mod/ lib/ src/*.f src/*.f90 bin/*.exe

echo "Clean complete."
