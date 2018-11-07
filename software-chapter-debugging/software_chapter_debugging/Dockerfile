FROM python:3.6.5-alpine3.7

ENV PROJECT_DIR /opt/alerts_om_processor
ENV SOURCE_DIR $PROJECT_DIR/source

# Adding Python requirements
COPY requirements ./requirements/

# Adding credentials for git cloning
ENV HOME /root
COPY .netrc $HOME/

# Install requirements
RUN apk add --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
     python3 git musl-dev postgresql-dev gcc geos && \
     python3 -m ensurepip && \
     rm -r /usr/lib/python*/ensurepip && \
     pip3 install setuptools && \
     if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
     if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
     rm -r /root/.cache

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

# Removing credentials and requirements
RUN rm -rf $HOME/.netrc
RUN rm -rf requirements

# Prepare source and scripts
RUN mkdir -p $SOURCE_DIR
COPY scripts /usr/local/bin
COPY source $SOURCE_DIR/

ENV PROJECT_ROOT $SOURCE_DIR

WORKDIR $PROJECT_DIR
CMD ["run"]
