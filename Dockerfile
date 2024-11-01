FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY services/ ./services/

EXPOSE 5000 5001
CMD ["python", "services/update_service.py"]
