import numpy as np
import plotly.express as px
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)

df = pd.DataFrame({"x":x, "y":y})

fig = px.line(df, x='x', y='y', title="Plotlt Sin Plot")
fig.show()