FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY spatialjoin_shp.py /app/spatialjoin_shp.py

ENTRYPOINT [ "python3", "/app/spatialjoin_shp.py" ]