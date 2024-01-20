from dotenv import load_dotenv
import os
import io
import requests
from urllib.request import urlopen
import json
from geojson import Feature, FeatureCollection, Point
import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.express as px
import plotly.graph_objects as go

# charger les tokens 
load_dotenv('.env')
TOKEN = os.getenv("TOKEN")
mapbox = os.getenv("MAPBOX")

headers = {'x-api-key': TOKEN, 'Content-Type':'application/json', 'private': 'true'}

# definir l'adresse de l'API
api2 = 'https://data.education.gouv.fr/api/v2'
api1 = 'https://www.data.gouv.fr/api/1/'

# Open session
session = requests.Session()

# Premier set de donnees pour obtenir le geoJSON des delimitations academiques de la France
r = session.get(f'{api2}/catalog/datasets/fr-en-contour-academies-2020/exports').json()
# Obtenir l'adresse URL donnant acces au data set
href_academies = r['links'][3]['href']
# Ouverture du data set
with urlopen(href_academies) as response:
    regions = json.load(response)