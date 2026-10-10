FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

COPY pyproject.toml ./
COPY src ./src
COPY sites*.toml ./
RUN pip install --no-cache-dir '.[all]'

# Körs som icke-root.
RUN useradd --create-home app
USER app

ENTRYPOINT ["shopify-sync"]
CMD ["run"]
