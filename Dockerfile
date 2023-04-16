FROM python:3.9-alpine3.13
LABEL maintainer="utolgaevren.com"

ENV PYTHONBUFFERED 1
COPY ./requirements.txt /app/requirements.txt
COPY ./requirements-dev.txt /app/requirements-dev.txt
COPY ./app /app
WORKDIR /app
#EXPOSE 5000
#EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r requirements-dev.txt ; \
    fi && \
    adduser \
        --disabled-password \
        --no-create-home \
        tolga-user

ENV PATH=/py/bin:$PATH


#ENTRYPOINT [ "python" ]

#CMD ["main.py"]

USER tolga-user

