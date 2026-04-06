import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# --- 1. SETTINGS & BRANDING ---
logo_path = "cofo-logo.jpg"

try:
    favicon = Image.open(logo_path)
    st.set_page_config(
        page_title="CofO | Particle-Wave Interference Lab", 
        page_icon=favicon, 
        layout="centered"
    )
except:
    st.set_page_config(
        page_title="CofO | Particle-Wave Interference Lab", 
        layout="centered"
    )

st.markdown("""
    <style>
        section[data-testid="stSidebar"] * {
            color: white !important;
        }
        section[data-testid="stSidebar"] input {
            color: #8D203C !important; 
        }
        .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp span {
            color: #000000;
        }
        [data-testid="stMetricLabel"] {
            color: #444444 !important;
        }
        [data-testid="stMetricValue"] {
            color: #000000 !important;
        }
        section[data-testid="stSidebar"] hr {
            border-top: 1px solid #ffffff44 !important;
        }
    </style>
""", unsafe_allow_html=True)

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.sidebar.image(logo, use_container_width=True)
else:
    st.sidebar.warning(f"Logo '{logo_path}' not found in repo.")

st.sidebar.markdown("### **College of the Ozarks**\nDepartment of Mathematics and Physics")
st.sidebar.divider()

col1, col2 = st.columns([1, 4]) 

with col1:
    if os.path.exists(logo_path):
        st.image(logo_path, width=128) 

with col2:
    st.markdown(f"""
        <h1 style='color: #8D203C; margin-bottom: 0; padding-top: 10px;'>Interference Lab</h1>
        <p style='color: #002147; font-style: italic; font-size: 1.5em; margin-top: 0;'>
        College of the Ozarks | "Hard Work U"
        </p>
    """, unsafe_allow_html=True)

st.markdown(r"""
    Welcome to the Particle-Wave Interference Lab! 

    When light passes through a narrow opening, it spreads out and creates a pattern of spots on a viewing screen. By measuring the distances between these spots, we can calculate the exact dimensions of the microscopic slits.
""")

# --- Updated Theory Section (Algebra-based) ---
with st.expander("💥 Wave-Particle Analysis & Synthesis Help"):
    st.markdown(r"""
    ### 1. The Small Angle Approximation
    In this lab, we assume the distance to the screen ($D$) is much larger than the slit width ($a$). This allows us to simplify the math by assuming:
    $$\sin \theta \approx \tan \theta \approx \frac{y}{D}$$
                
    ### 2. Single Slit (Diffraction)
    For a single opening, the light cancels itself out at specific points, creating **dark spots (minima)**. The distance ($y$) from the center line to the $m^{th}$ dark spot is given by the formula:
    $$y = \frac{m \lambda L}{a}$$
    Where:
    * **$m$**: Order of the dark spot (1 for the first dark spot, 2 for the second, etc.)
    * **$\lambda$**: Wavelength of the laser light
    * **$L$**: Distance from the slit to the screen
    * **$a$**: Width of the single slit

    **Lab Tip:** In your sketch, you will measure the total distance between the dark spots on *both* sides of the center. To find $y$, simply divide your total measured distance by 2. You can then rearrange the formula to solve for the slit width: **$a = \frac{m \lambda L}{y}$**

    ### 3. Double Slit (Interference)
    When light passes through two slits side-by-side, the waves overlap to create sharp **bright spots (maxima)**. The distance ($y$) from the center to the $m^{th}$ bright spot is:
    $$y = \frac{m \lambda L}{d}$$
    Where **$d$** is the separation distance between the two slits. 
    *(Note: You will also see the broader single-slit "envelope" causing the bright spots to fade out at the diffraction minima!)*

    ### 4. Percent Error ($\epsilon_r$)
    To check the accuracy of your experimental measurement against the theoretical value, use the percent error formula:
    $$\epsilon_r = \left| \frac{\text{Experimental} - \text{Theoretical}}{\text{Theoretical}} \right| \times 100\%$$

    **Example:**
    If the theoretical slit width is **40.0 μm** and your calculated experimental value is **38.5 μm**:
    1. Subtract: $38.5 - 40.0 = -1.5$
    2. Take absolute value: $1.5$
    3. Divide by theoretical: $1.5 / 40.0 = 0.0375$
    4. Multiply by 100: **3.75% error**
    """)

# --- 2. Sidebar: Experimental Parameters ---
st.sidebar.header("1. Laser Settings")
mode = st.sidebar.radio("Configuration", ["Single Slit", "Double Slit"])
lam_nm = st.sidebar.slider("Wavelength [nm]", 400, 700, 670, step=1)
lam = lam_nm * 1e-9 

st.sidebar.header("2. Slit Geometry")
a_um = st.sidebar.slider("Slit Width (a) [μm]", 10, 200, 40, step=10)
a = a_um * 1e-6 

if mode == "Double Slit":
    d_um = st.sidebar.slider("Slit Separation (d) [μm]", 50, 600, 125, step=10)
    d = d_um * 1e-6
else:
    d = 0.0

st.sidebar.header("3. Environment")
L = st.sidebar.number_input("Distance to Screen (L) [m]", value=0.7, step=0.1)
exposure = st.sidebar.slider("Visual Exposure (Gain)", 0.01, 1.0, 0.2)

# --- NEW: Student Math Check Inputs ---
st.sidebar.header("4. Math Check")
if mode == "Single Slit":
    student_val = st.sidebar.number_input("Your Calculated 'a' [μm]", value=0.0, step=0.1)
    true_val = a_um
else:
    student_val = st.sidebar.number_input("Your Calculated 'd' [μm]", value=0.0, step=0.1)
    true_val = d_um

# --- 3. Physics & Math Logic ---
y_null_mm = (L * lam / a) * 1000
zoom_limit = y_null_mm * (2.5 if mode == "Single Slit" else 1.5)
zoom_limit = max(min(zoom_limit, 200.0), 5.0) 

y_pts = np.linspace(-zoom_limit/1000, zoom_limit/1000, 3000)
theta = np.arctan(y_pts / L)

beta = (a * np.sin(theta)) / lam
I_final = np.sinc(beta)**2

if mode == "Double Slit":
    alpha = (np.pi * d * np.sin(theta)) / lam
    I_final *= (np.cos(alpha)**2)

w = 100.0 * 1e-3
I_final *= np.exp(-2 * (y_pts**2) / (w**2))

# --- 4. UI: Results & Metrics ---
st.subheader("Lab Analysis Results [mm]")
laser_color = '#FF0000' if lam_nm >= 600 else '#00FF00' if lam_nm >= 495 else '#0000FF' if lam_nm >= 450 else '#8A2BE2'

# 1. Calculation Logic (No NaN)
if student_val > 0:
    calc_error = (abs(student_val - true_val) / true_val) * 100
    error_display = f"{calc_error:.1f}%"
else:
    error_display = "---"

# 2. Render Metrics
if mode == "Double Slit":
    c1, c2, c3, c4, c5 = st.columns(5)
    
    env_dist = (2 * lam * L / a) * 1000
    int_min1 = (lam * L / d) * 1000
    int_max1 = (2 * lam * L / d) * 1000
    int_max2 = (4 * lam * L / d) * 1000

    # Use shorter labels to prevent truncation/overflow
    c1.metric("Envelope (m=1)", f"{env_dist:.2f}")
    c2.metric("Int. Min. (m=1)", f"{int_min1:.2f}")
    c3.metric("Int. Max. (m=1)", f"{int_max1:.2f}")
    c4.metric("Int. Max. (m=2)", f"{int_max2:.2f}")
    c5.metric("% Error (d)", error_display)

else:
    c1, c2, c3 = st.columns(3)
    
    m1_dist = (2 * lam * L / a) * 1000
    m2_dist = (4 * lam * L / a) * 1000
    
    c1.metric("Minima Dist. (m=1)", f"{m1_dist:.2f}")
    c2.metric("Minima Dist. (m=2)", f"{m2_dist:.2f}")
    c3.metric("% Error (a)", error_display)

# --- 5. UI: Visualization ---
fig1, ax1 = plt.subplots(figsize=(12, 3.5))
ax1.plot(y_pts * 1000, I_final, color=laser_color, lw=2)
ax1.fill_between(y_pts * 1000, I_final, color=laser_color, alpha=0.15)
ax1.set_xlim(-zoom_limit, zoom_limit)
ax1.set_ylim(0, 1.05)
ax1.set_xlabel("Screen Position (mm)")
ax1.set_ylabel("Relative Intensity")
st.pyplot(fig1)

st.markdown("### Simulated Screen View")
y_vert = np.linspace(-3, 3, 100) 
X_grid, Y_grid = np.meshgrid(y_pts * 1000, y_vert)
vert_fade = np.exp(-2 * (Y_grid**2) / (1.5**2)) 
I_2d = I_final * vert_fade

from matplotlib.colors import LinearSegmentedColormap
laser_cmap = LinearSegmentedColormap.from_list("laser", [(0,0,0), laser_color])

fig2, ax2 = plt.subplots(figsize=(12, 1.2))
ax2.imshow(I_2d, extent=[-zoom_limit, zoom_limit, -3, 3], aspect='auto', cmap=laser_cmap, vmax=exposure)
ax2.axis('off')
st.pyplot(fig2)