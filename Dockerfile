FROM python:3.6
RUN pip install nbconvert==5.6.0 notebook==5.6.0
RUN pip install "pelican[markdown]" pelican-jupyter ghp-import
WORKDIR /caverna
ENTRYPOINT ["make", "serve-global", "PORT=8080"]