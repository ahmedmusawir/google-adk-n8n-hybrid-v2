#!/bin/bash

# adk api_server . --host=0.0.0.0 --port=8000 --session_service_uri='postgresql+psycopg2://postgres:Key%40mony5392@172.23.48.3:5432/adk_sessions' DID NOT WORK

adk api_server . --host=0.0.0.0 --port=8000 --session_service_uri='postgresql+psycopg2://postgres:Key%40mony5392@127.0.0.1:5432/adk_sessions'