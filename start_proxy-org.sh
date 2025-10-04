#!/bin/bash

# This script starts the Cloud SQL Auth Proxy for the ADK v2 session store.

echo "🚀 Starting Cloud SQL Auth Proxy..."
echo "   Connecting to: adk-v2-session-store"
echo "   Listening on: localhost:5432"
echo "--------------------------------------------------"

# Run the proxy command. The script will wait here until you stop it (Ctrl+C).
./cloud-sql-proxy ninth-potion-455712-g9:us-east1:adk-v2-session-store --port 5432
#
# Add the --private-ip flag to use the secure internal connection
# ./cloud-sql-proxy --private-ip ninth-potion-455712-g9:us-east1:adk-v2-session-store --port 5432

# ./cloud-sql-proxy --private-ip ninth-potion-455712-g9:us-east1:adk-v2-session-store 
