FROM ubuntu:24.04
WORKDIR /app
COPY calculator.py test_calculator.py ./
RUN apt-get update && apt-get install -y --no-install-recommends python3-pytest \
    && rm -rf /var/lib/apt/lists/*
CMD ["python3", "-m", "pytest", "-v"]
