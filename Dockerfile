FROM fnproject/python:3.8-dev as build-stage
WORKDIR /function
ADD requirements.txt /function/
ADD srch.crt /function
RUN pip3 install --target /python/ --no-cache --no-cache-dir -r requirements.txt elasticsearch datetime && rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv
ADD . /function/
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.8
WORKDIR /function
COPY --from=build-stage /function /function
COPY --from=build-stage /python /python
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]
