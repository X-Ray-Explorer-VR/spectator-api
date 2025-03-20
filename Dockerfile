FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask environment
ENV IP="0.0.0.0"
ENV PORT=5000

# MariaDB connection
ENV DB_HOST="localhost"
ENV DB_USER="root"
ENV DB_PASSWORD=""
ENV DB_NAME="skeleton"

EXPOSE ${PORT}

CMD ["python", "api_server.py", "--host=${IP}", "--port=${PORT}"]