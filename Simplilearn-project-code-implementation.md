```
Microsoft Windows [Version 10.0.26100.4770]
(c) Microsoft Corporation. All rights reserved.

C:\Users\AMULYAK>cd simplilearn-capstone-project-amulya

C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya>python -m venv venv

C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya>venv\Scripts\activate

(venv) C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya>pip install -r requirements_1.txt
Collecting streamlit==1.28.2
  Downloading streamlit-1.28.2-py2.py3-none-any.whl (8.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.4/8.4 MB 11.7 MB/s eta 0:00:00
Collecting pandas==2.1.0
  Downloading pandas-2.1.0-cp311-cp311-win_amd64.whl (11.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.0/11.0 MB 13.1 MB/s eta 0:00:00
Collecting numpy==1.24.3
  Downloading numpy-1.24.3-cp311-cp311-win_amd64.whl (14.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.8/14.8 MB 14.5 MB/s eta 0:00:00
Collecting matplotlib==3.7.2
  Downloading matplotlib-3.7.2-cp311-cp311-win_amd64.whl (7.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 17.1 MB/s eta 0:00:00
Collecting seaborn==0.12.2
  Downloading seaborn-0.12.2-py3-none-any.whl (293 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 293.3/293.3 kB 18.9 MB/s eta 0:00:00
Collecting plotly==5.17.0
  Downloading plotly-5.17.0-py2.py3-none-any.whl (15.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.6/15.6 MB 12.6 MB/s eta 0:00:00
Collecting scikit-learn==1.3.1
  Downloading scikit_learn-1.3.1-cp311-cp311-win_amd64.whl (9.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 12.5 MB/s eta 0:00:00
Collecting statsmodels==0.14.0
  Downloading statsmodels-0.14.0-cp311-cp311-win_amd64.whl (9.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.2/9.2 MB 19.0 MB/s eta 0:00:00
Collecting openpyxl==3.1.2
  Downloading openpyxl-3.1.2-py2.py3-none-any.whl (249 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.0/250.0 kB 16.0 MB/s eta 0:00:00
Collecting altair<6,>=4.0
  Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Collecting blinker<2,>=1.0.0
  Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting cachetools<6,>=4.0
  Using cached cachetools-5.5.2-py3-none-any.whl (10 kB)
Collecting click<9,>=7.0
  Using cached click-8.2.1-py3-none-any.whl (102 kB)
Collecting importlib-metadata<7,>=1.4
  Downloading importlib_metadata-6.11.0-py3-none-any.whl (23 kB)
Collecting packaging<24,>=16.8
  Downloading packaging-23.2-py3-none-any.whl (53 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 2.9 MB/s eta 0:00:00
Collecting pillow<11,>=7.1.0
  Downloading pillow-10.4.0-cp311-cp311-win_amd64.whl (2.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 14.8 MB/s eta 0:00:00
Collecting protobuf<5,>=3.20
  Downloading protobuf-4.25.8-cp310-abi3-win_amd64.whl (413 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 413.7/413.7 kB 13.0 MB/s eta 0:00:00
Collecting pyarrow>=6.0
  Downloading pyarrow-21.0.0-cp311-cp311-win_amd64.whl (26.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.2/26.2 MB 11.9 MB/s eta 0:00:00
Collecting python-dateutil<3,>=2.7.3
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting requests<3,>=2.27
  Using cached requests-2.32.4-py3-none-any.whl (64 kB)
Collecting rich<14,>=10.14.0
  Using cached rich-13.9.4-py3-none-any.whl (242 kB)
Collecting tenacity<9,>=8.1.0
  Downloading tenacity-8.5.0-py3-none-any.whl (28 kB)
Collecting toml<2,>=0.10.1
  Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting typing-extensions<5,>=4.3.0
  Downloading typing_extensions-4.14.1-py3-none-any.whl (43 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.9/43.9 kB 2.1 MB/s eta 0:00:00
Collecting tzlocal<6,>=1.1
  Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
Collecting validators<1,>=0.2
  Downloading validators-0.35.0-py3-none-any.whl (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.7/44.7 kB 1.1 MB/s eta 0:00:00
Collecting gitpython!=3.1.19,<4,>=3.0.7
  Downloading gitpython-3.1.45-py3-none-any.whl (208 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 208.2/208.2 kB 6.4 MB/s eta 0:00:00
Collecting pydeck<1,>=0.8.0b4
  Using cached pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
Collecting tornado<7,>=6.0.3
  Using cached tornado-6.5.1-cp39-abi3-win_amd64.whl (444 kB)
Collecting watchdog>=2.1.5
  Using cached watchdog-6.0.0-py3-none-win_amd64.whl (79 kB)
Collecting pytz>=2020.1
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting tzdata>=2022.1
  Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.3-cp311-cp311-win_amd64.whl (225 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 225.2/225.2 kB 13.4 MB/s eta 0:00:00
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.59.0-cp311-cp311-win_amd64.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 20.7 MB/s eta 0:00:00
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.4.8-cp311-cp311-win_amd64.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 72.0/72.0 kB 4.1 MB/s eta 0:00:00
Collecting pyparsing<3.1,>=2.3.1
  Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.3/98.3 kB 5.9 MB/s eta 0:00:00
Collecting scipy>=1.5.0
  Downloading scipy-1.16.1-cp311-cp311-win_amd64.whl (38.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.6/38.6 MB 9.9 MB/s eta 0:00:00
Collecting joblib>=1.1.1
  Downloading joblib-1.5.1-py3-none-any.whl (307 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 307.7/307.7 kB 9.6 MB/s eta 0:00:00
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Collecting patsy>=0.5.2
  Downloading patsy-1.0.1-py2.py3-none-any.whl (232 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.9/232.9 kB 7.2 MB/s eta 0:00:00
Collecting et-xmlfile
  Using cached et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Collecting jinja2
  Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Collecting jsonschema>=3.0
  Downloading jsonschema-4.25.0-py3-none-any.whl (89 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 89.2/89.2 kB 4.9 MB/s eta 0:00:00
Collecting narwhals>=1.14.2
  Downloading narwhals-2.0.1-py3-none-any.whl (385 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 385.4/385.4 kB 23.4 MB/s eta 0:00:00
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.2-cp311-cp311-win_amd64.whl (222 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 222.0/222.0 kB 6.6 MB/s eta 0:00:00
Collecting gitdb<5,>=4.0.1
  Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Collecting zipp>=0.5
  Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Collecting six>=1.5
  Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting charset_normalizer<4,>=2
  Using cached charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl (105 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.10-py3-none-any.whl (70 kB)
Collecting urllib3<3,>=1.21.1
  Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 161.2/161.2 kB 9.4 MB/s eta 0:00:00
Collecting markdown-it-py>=2.2.0
  Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting pygments<3.0.0,>=2.13.0
  Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 19.6 MB/s eta 0:00:00
Collecting scipy>=1.5.0
  Downloading scipy-1.16.0-cp311-cp311-win_amd64.whl (38.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.6/38.6 MB 10.6 MB/s eta 0:00:00
  Downloading scipy-1.15.3-cp311-cp311-win_amd64.whl (41.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.2/41.2 MB 9.6 MB/s eta 0:00:00
Collecting smmap<6,>=3.0.1
  Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl (15 kB)
Collecting attrs>=22.2.0
  Using cached attrs-25.3.0-py3-none-any.whl (63 kB)
Collecting jsonschema-specifications>=2023.03.6
  Using cached jsonschema_specifications-2025.4.1-py3-none-any.whl (18 kB)
Collecting referencing>=0.28.4
  Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting rpds-py>=0.7.1
  Downloading rpds_py-0.26.0-cp311-cp311-win_amd64.whl (231 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 231.7/231.7 kB 7.1 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pytz, zipp, watchdog, validators, urllib3, tzdata, typing-extensions, tornado, toml, threadpoolctl, tenacity, smmap, six, rpds-py, pyparsing, pygments, pyarrow, protobuf, pillow, packaging, numpy, narwhals, mdurl, MarkupSafe, kiwisolver, joblib, idna, fonttools, et-xmlfile, cycler, colorama, charset_normalizer, certifi, cachetools, blinker, attrs, tzlocal, scipy, requests, referencing, python-dateutil, plotly, patsy, openpyxl, markdown-it-py, jinja2, importlib-metadata, gitdb, contourpy, click, scikit-learn, rich, pydeck, pandas, matplotlib, jsonschema-specifications, gitpython, statsmodels, seaborn, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.2 altair-5.5.0 attrs-25.3.0 blinker-1.9.0 cachetools-5.5.2 certifi-2025.8.3 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 contourpy-1.3.2 cycler-0.12.1 et-xmlfile-2.0.0 fonttools-4.59.0 gitdb-4.0.12 gitpython-3.1.45 idna-3.10 importlib-metadata-6.11.0 jinja2-3.1.6 joblib-1.5.1 jsonschema-4.25.0 jsonschema-specifications-2025.4.1 kiwisolver-1.4.8 markdown-it-py-3.0.0 matplotlib-3.7.2 mdurl-0.1.2 narwhals-2.0.1 numpy-1.24.3 openpyxl-3.1.2 packaging-23.2 pandas-2.1.0 patsy-1.0.1 pillow-10.4.0 plotly-5.17.0 protobuf-4.25.8 pyarrow-21.0.0 pydeck-0.9.1 pygments-2.19.2 pyparsing-3.0.9 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 requests-2.32.4 rich-13.9.4 rpds-py-0.26.0 scikit-learn-1.3.1 scipy-1.15.3 seaborn-0.12.2 six-1.17.0 smmap-5.0.2 statsmodels-0.14.0 streamlit-1.28.2 tenacity-8.5.0 threadpoolctl-3.6.0 toml-0.10.2 tornado-6.5.1 typing-extensions-4.14.1 tzdata-2025.2 tzlocal-5.3.1 urllib3-2.5.0 validators-0.35.0 watchdog-6.0.0 zipp-3.23.0

[notice] A new release of pip available: 22.3.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya>python data-generator.py
Generating sales data...
Traceback (most recent call last):
  File "C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya\data-generator.py", line 52, in <module>
    month = date.month
            ^^^^^^^^^^
AttributeError: 'numpy.datetime64' object has no attribute 'month'

(venv) C:\Users\Venkat Kaza\Simplilearn-capstone-project-Amulya>python data_generator.py
Generating sales data...
Generated 500 records...
Generated 1000 records...
Generated 1500 records...
Generated 2000 records...
Generated 2500 records...

Successfully generated 2500 sales records!
Data saved to: sales_data.csv

Data Summary:
- Date range: 2023-01-01 to 2023-12-31
- Total sales: $1,017,582.36
- Average sale: $407.03
- Number of products: 15
- Number of regions: 5

Sample data (first 5 rows):
           Date         Product  ... Customer_Gender  Customer_Satisfaction
433  2023-01-01      Hard Drive  ...          Female                    4.4
806  2023-01-01  Gaming Console  ...            Male                    4.6
626  2023-01-01           Mouse  ...            Male                    4.1
747  2023-01-01         Monitor  ...            Male                    3.4
89   2023-01-01          Tablet  ...          Female                    3.3

[5 rows x 7 columns]

(venv) C:\Users\AMULYAK\Simplilearn-capstone-project-Amulya>streamlit run simplilearn-projectx.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.36:8501
```
