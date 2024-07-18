FROM python:3.10.14-slim

COPY requirements.txt /tmp/pip-tmp/

RUN python3 -m pip --disable-pip-version-check --no-cache-dir install --trusted-host mkmartifactory.amd.com -r /tmp/pip-tmp/requirements.txt

COPY sum.py /app/sum.py

EXPOSE 8800

WORKDIR /app

CMD ["python3", "/app/sum.py"]
