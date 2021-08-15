FROM python:3.8.10
WORKDIR /mnt/c/User/Brenno/Documents/PyCodes/FastAPI
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD uvicorn --reload --host=0.0.0.0 --port=8000 blog.main:app