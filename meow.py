import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("🦋 мейд бай кувшинка")
st.markdown(r"""###формула этого метелика
    $$
x(t) = \sin(t) \cdot \left(e^{\cos(t)} - 2\cos(4t) + \sin^5\left(\frac{t}{12}\right)\right)
$$

$$
y(t) = \cos(t) \cdot \left(e^{\cos(t)} - 2\cos(4t) + \sin^5\left(\frac{t}{12}\right)\right)
$$

**интервал:**  

$$ t \in [0,\ 12\pi] $$
""")


k = st.slider(
    "max значение тешки: t = k·π",    
    min_value=1, max_value=20,     
    value=12                       
)

num_points = st.slider(
    "Количество точек (точность)",
    min_value=500, max_value=3000,
    value=1000, step=100
)

color = st.selectbox(
    "Цвет кривой",
    options=["purple", "blue", "red", "green", "black", "orange", "pink",],
    index=0
) 

sin_power = st.slider("Степень синуса (sin(t/12)^n)", min_value=1, max_value=50, value=5)


t = np.linspace(0, k * np.pi, num_points)

expression = np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**sin_power
x = np.cos(t) * expression
y = np.sin(t) * expression 

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(y, x, color = color)
ax.set_title("Кривая бабочки")
ax.axis('equal')
ax.grid(True)

st.pyplot(fig)