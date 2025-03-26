FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask environment
ENV PORT=5000

EXPOSE ${PORT}

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
