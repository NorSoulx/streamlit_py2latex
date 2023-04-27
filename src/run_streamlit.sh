#!/bin/bash
echo "Running Streamlit app"
PORT=8501
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

