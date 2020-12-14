FROM python:3.8-slim
RUN pip install --no-cache-dir discord.py requests

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL maintainer="RoberthStrand" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="RobotSatoshi" \
    org.label-schema.description="A Discord bot for displaying bitcoin prices" \
    org.label-schema.url="https://robstr.dev" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/roberthstrand/RobotSatoshi" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"

COPY /src /app

# RUN ln -sf /dev/stdout /var/log/robotsatoshi.log

ENTRYPOINT [ "python3", "/app/robotsatoshi.py" ]