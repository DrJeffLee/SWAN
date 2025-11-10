#!/bin/bash
set -e # Exit on error

# Execute from the top-level SWAN directory
cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")"

# Create build directory if it doesn't exist
mkdir -p build

# Configure with Ninja
# cmake -S . -B build -G Ninja -DCMAKE_INSTALL_PREFIX="$(pwd)"
cmake -S . -B build -G Ninja

# Build
cmake --build build

# Install
cmake --install build
