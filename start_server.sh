#!/bin/bash

# Start ADK server with Supabase
adk api_server . \
  --host=0.0.0.0 \
  --port=8000 \
  --session_service_uri='postgresql://postgres.zldxzlbkoayhyhzxpjrq:Keyamony5392@aws-0-us-east-1.pooler.supabase.com:5432/postgres?sslmode=require'