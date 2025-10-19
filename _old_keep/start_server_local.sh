#!/bin/bash

adk api_server .   --host=0.0.0.0   --port=8000   --session_service_uri='sqlite:///adk_sessions.db'
