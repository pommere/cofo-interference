# Wave Optics: Single and Double Slit Simulator

This interactive web application is designed to simulate **Fraunhofer diffraction** and interference patterns for undergraduate physics laboratories. It allows students to explore the mathematical relationships between wavelength, slit geometry, and screen distance in real-time.

This project is a component of the laboratory curriculum for *A Modern Introduction to Physical Science*.

## 🔬 Physics Overview

The application models the relative intensity $I$ as a function of the position on the screen $y$.

### The Model
The simulator uses the standard diffraction and interference equations. For a double-slit configuration, the intensity is calculated as:

$$I(\theta) = I_0 \left( \frac{\sin \beta}{\beta} \right)^2 \cos^2 \alpha$$

Where:
* $\beta = \frac{\pi a \sin \theta}{\lambda}$ (Single-slit envelope)
* $\alpha = \frac{\pi d \sin \theta}{\lambda}$ (Interference term)
* $a$ is the slit width and $d$ is the slit separation.

### Gaussian Beam Profile
Unlike idealized models that assume a uniform plane wave, this simulator includes an option to model a **Gaussian laser distribution**. This accounts for the natural spatial decay of intensity from the center of the laser source, providing a more accurate representation of what students observe in a physical lab setting.

## 🚀 Features

* **Toggle Modes:** Switch between Single Slit and Double Slit configurations.
* **Dynamic Inputs:** Real-time adjustment of:
    * Wavelength ($\lambda$) in nanometers.
    * Slit width ($a$) and separation ($d$) in micrometers.
    * Screen distance ($L$) in meters.
* **Interactive Visualization:** High-resolution plots showing intensity distributions and predicted maxima ($m_1, m_2, \dots$).
* **Gaussian Modeling:** Optional beam-waist adjustments to simulate realistic laser spread.

## 🛠️ Local Setup

To run this application locally, ensure you have Python installed, then:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/pommere/diffraction-lab.git](https://github.com/pommere/diffraction-lab.git)
   cd diffraction-lab