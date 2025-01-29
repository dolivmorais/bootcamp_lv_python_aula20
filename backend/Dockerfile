FROM python:3.10

WORKDIR /app

COPY requirements.txt .  
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .  # Isso garante que manage.py será copiado

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
