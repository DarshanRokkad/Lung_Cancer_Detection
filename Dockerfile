FROM python:3.11-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app
RUN pip install -r deployment_requirements.txt
CMD streamlit run --server.port 80 app.py