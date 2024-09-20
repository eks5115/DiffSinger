FROM python:3.11.9 as builder
WORKDIR /build
COPY ./requirements.txt /build/requirements.txt
RUN apt update && apt install -y libhdf5-dev
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip,sharing=shared \
    pip install -i https://mirrors.aliyun.com/pypi/simple -r /build/requirements.txt

FROM python:3.11.9-slim
EXPOSE 8000
WORKDIR /var/web
RUN apt update && apt install -y libhdf5-dev \
    && apt purge \
      && apt autoremove \
      && apt clean \
      && rm -rf /var/lib/apt/lists/* \
      && rm -rf /tmp/*
ENV PYTHONPATH /var/web
ENTRYPOINT ["fastapi","run"]
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/fastapi /usr/local/bin/fastapi
COPY ./ /var/web
