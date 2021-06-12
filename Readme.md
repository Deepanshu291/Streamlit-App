
![Logo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

    
# Streamlit First App

Streamlit turns data scripts into shareable web apps in minutes.
All in Python. All for free. No front‑end experience required.



## Deployment

To install this project packages

```bash
   pip install -r requirement.txt
```

To deploy this project run

```bash
   streamlit run app.py
```

  
## Usage/Examples

```python
import streamlit as st
import pandas as pd
import numpy  as np

st.write("""
# welcome to Streamlit App
Here is *data!*
This is My First App
""")

dt = pd.read_csv("./sample.csv")
st.line_chart(dt)

```

  
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## Acknowledgements

 - [Streamlit Documentation](https://docs.streamlit.io/en/stable/index.html)
 - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

  
## Authors

- [@Deepanshu Sharma](https://github.com/Deepanshu291)

  