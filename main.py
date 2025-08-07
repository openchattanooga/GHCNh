# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "geopandas",
#     "pandas",
#     "pyarrow",
#     "requests",
# ]
# ///

import geopandas as gpd
import io
import pandas as pd
import requests

longitude = -85.3116
latitude = 35.0439

# station ids https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
url = "https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-station/GHCNh_USW00013882_por.psv"

fcsv = io.StringIO(requests.get(url).text)
df = pd.read_csv(fcsv, sep='|', low_memory=False)
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']), crs="EPSG:4326"
)

print("gdfhead:", gdf.head())

gdf.to_parquet("GHCNh_USW00013882_por.parquet")
