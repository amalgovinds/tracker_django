FROM python:3.11-slim AS base
WORKDIR /opt/app/tracker
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt /opt/app/tracker
RUN pip install -r requirements.txt
COPY . /opt/app/tracker
CMD ["python", "manage.py", "runserver"]
# FROM python:3.11-slim as compiler
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app/

# RUN python -m venv /opt/venv
# # Enable venv
# ENV PATH="/opt/venv/bin:$PATH"

# COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt

# FROM python:3.11-slim as runner
# WORKDIR /app/
# COPY --from=compiler /opt/venv /opt/venv

# # Enable venv
# ENV PATH="/opt/venv/bin:$PATH"
# COPY . /app/
# EXPOSE 8080
# CMD ["python", "manage.py", "runserver"]