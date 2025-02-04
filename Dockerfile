FROM python:3.10-slim AS base

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY weather_app weather_app/


FROM base AS tests

RUN pip install pytest

COPY tests tests/

RUN python -m pytest tests/


FROM base

CMD ["python", "-m", "weather_app"]
