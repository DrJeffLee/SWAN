#!/bin/bash
set -e # Exit on error

# Set root directory
SWAN_DIR="$(dirname "$(dirname "${BASH_SOURCE[0]}")")"
SWAN_DIR="$(readlink -f "$SWAN_DIR")"

echo "Settting paths..."

# Directories to add
BIN_DIR="$SWAN_DIR/bin"
#LIB_DIR="$SWAN_DIR/lib"

# Export paths
export PATH="$PATH:$BIN_DIR"
#export LD_LIBRARY_PATH="$LIB_DIR:$LD_LIBRARY_PATH"

echo "Environment updated:"
#echo "  SWAN_DIR=$SWAN_DIR"
echo "  BIN_DIR=$BIN_DIR"
#echo "  LIB_DIR=$LIB_DIR"
