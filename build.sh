#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")" # Executes from the directory containing the script
set -e # Exit on error

# Create build directory if it doesn't exist
mkdir -p build

# Configure with Ninja
cmake -S . -B build -G Ninja -DCMAKE_INSTALL_PREFIX="$(pwd)"

# Build
cmake --build build

# Install
cmake --install build
