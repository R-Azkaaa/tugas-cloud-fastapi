FROM python:3.9-slim
WORKDIR /app
COPY source-code/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "source-code.main:app", "--host", "0.0.0.0", "--port", "8000"]
