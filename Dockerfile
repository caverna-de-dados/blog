FROM python:3.8
RUN pip install "pelican[markdown]" pelican-jupyter ghp-import
WORKDIR /caverna
ENTRYPOINT ["make", "serve-global", "PORT=8080"]