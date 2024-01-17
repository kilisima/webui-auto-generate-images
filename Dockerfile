FROM python:3.11.7-slim-bookworm

# WORKDIR /app
RUN mkdir -p /storage && chmod 777 /storage

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/streamlit/streamlit-example.git .
COPY app app
COPY main.sh main.sh
COPY requirements.txt requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]