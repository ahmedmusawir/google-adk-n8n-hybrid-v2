#!/bin/bash

if [ -f "$SCRIPT_DIR/.env" ]; then
  set -a; source "$SCRIPT_DIR/.env"; set +a
else
  echo ".env not found, assuming environment vars are already set."
fi


echo $GOOGLE_PROJECT_ID
echo $GOOGLE_LOCATION
echo $GOOGLE_APPLICATION_CREDENTIALS


# CLOUD SQL ACCESS VIA LOCAL CLOUD SQL PROXY
# adk api_server . --host=0.0.0.0 --port=8000 --session_service_uri='postgresql+psycopg2://postgres:Key%40mony5392@127.0.0.1:5432/adk_sessions'

# FOR SUPABASE POSTGRESQL (QR PROJECT STAGING) DEPRECATED
#  adk api_server .   --port=8000   --session_db_url='postgresql://postgres.zldxzlbkoayhyhzxpjrq:Keyamony5392@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require'

# Export the required environment variables for the Vertex AI client
# export GOOGLE_PROJECT_ID="ninth-potion-455712-g9"
# export GOOGLE_LOCATION="us-central1"

# FOR SUPABASE POSTGRESQL (QR PROJECT STAGING)
adk api_server . \
  --host=0.0.0.0 \
  --port=8000 \
  --session_service_uri='postgresql://postgres.zldxzlbkoayhyhzxpjrq:Keyamony5392@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require'