import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
national_url = 'https://www.huduser.gov/portal/datasets/hads/hads2013n_ASCII.zip
national_file = 'thads2013n.txt'
z_national = urlopen(national_url)
zip_national = ZipFile(BytesIO(z_national.read())).extract(national_file)
df_national = pd.read_csv(zip_national)
df_national.info()
df_national.head()
