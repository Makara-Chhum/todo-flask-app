FROM python:3.11.4-alpine3.18

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# CMD [ "python", "app.py" ]
CMD flask --app app.py run --debug --host=0.0.0.0