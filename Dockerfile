FROM python:3.12-slim
WORKDIR /app
COPY vendor /opt/vendor
ENV PYTHONPATH=/opt/vendor
COPY calculator.py test_calculator.py ./
CMD ["python", "-m", "pytest", "-v"]
