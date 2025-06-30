import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D

st.title("мейд бай кувшинка") 

figure = st.selectbox("Выбрать кривую", ["Кривая бабочки", "Поверхности Дини"])


if figure == "Кривая бабочки":
   st.markdown(r"""
   ### формула єтого метелика:

   $$
   x(t) = \sin(t) \cdot \left(e^{\cos(t)} - 2\cos(4t) + \sin^5\left(\frac{t}{12}\right)\right)
   $$

   $$
   y(t) = \cos(t) \cdot \left(e^{\cos(t)} - 2\cos(4t) + \sin^5\left(\frac{t}{12}\right)\right)
   $$

   $$ Интервал:  

   t \in [0;\ 12\pi]
   $$
   """)

   k = st.slider(
    "Max значение тешки:",    
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
    index=1
   ) 

   sin_power = st.slider("Степень синуса:", min_value=1, max_value=50, value=5)


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
   pass

elif figure == "Поверхности Дини":
    
   st.markdown(r"""### формула:
 
   $$
   x(t) = \cos(u) \cdot \sin(v)
   $$

   $$
   y(t) = b\sin(u) \cdot b\sin(v)
   $$ 

   $$ 
   z(t) = b\cos(v) + \log_{10}\left(\tan\left(\frac{v}{2}\right)\right) + b \cdot u
   $$ 

   $$ 
   u \in [0;\ 4\pi], v \in [0,001;\ 2]
   $$ 

   """)

   cmap = st.sidebar.selectbox ("Цвет",
    options = ["plasma", "viridis", "inferno", "coolwarm"], 
    index = 0)


   u_max = st.sidebar.slider("Максимум u", np.pi, 10 * np.pi, 4 * np.pi, step=np.pi)  
   v_min = st.sidebar.slider("Минимум v", 0.001, 1.0, 0.001)
   v_max = st.sidebar.slider("Максимум v", 0.1, 4.0, 2.0)

   scale = st.sidebar.slider("Коеф наклона", 0.0, 1.0, 0.2)  
   offset = st.sidebar.slider("Z-смещение", -10.0, 10.0, -4.0)   

   u = np.linspace(0, u_max, 200)
   v = np.linspace(v_min, v_max, 100)
   u, v = np.meshgrid(u, v) 

   x = np.cos(u) * np.sin(v)
   y = np.sin(u) * np.sin(v)
   z = np.cos(v) + np.log10(np.tan(v / 2)) + scale * u + offset

   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')

   surface = ax.plot_surface(x, y, z, cmap=cmap, edgecolor='k', linewidth=0.3, antialiased=True)

   ax.set_xlabel('X')
   ax.set_ylabel('Y')
   ax.set_zlabel('Z')
   ax.set_title('Поверхность Дини')


   st.pyplot(fig)