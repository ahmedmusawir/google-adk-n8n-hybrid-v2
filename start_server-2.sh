#!/bin/bash
set -e  # Exit on error

# Load environment variables
if [ -f .env ]; then
    echo "Loading .env file..."
    set -a
    source .env
    set +a
else
    echo "ERROR: .env file not found!"
    exit 1
fi

# Verify critical vars
if [ -z "$GOOGLE_PROJECT_ID" ]; then
    echo "ERROR: GOOGLE_PROJECT_ID not set in .env"
    exit 1
fi

if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "ERROR: GOOGLE_APPLICATION_CREDENTIALS not set in .env"
    exit 1
fi

if [ ! -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "ERROR: Credentials file not found at $GOOGLE_APPLICATION_CREDENTIALS"
    exit 1
fi

echo "Environment loaded successfully"
echo "Project: $GOOGLE_PROJECT_ID"
echo "Location: $GOOGLE_LOCATION"
echo "Creds: $GOOGLE_APPLICATION_CREDENTIALS"

# Start ADK server with Supabase
adk api_server . \
  --host=0.0.0.0 \
  --port=8000 \
  --session_service_uri='postgresql://postgres.zldxzlbkoayhyhzxpjrq:Keyamony5392@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require'