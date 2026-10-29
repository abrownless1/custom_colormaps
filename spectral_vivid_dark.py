# Modification on the matplotlib spectral colormap to be brighter, with more contrast among colors. 

import numpy as np
import matplotlib as mpl
from matplotlib.colors import (
    LinearSegmentedColormap, rgb_to_hsv, hsv_to_rgb
)

# Start with Spectral
base_cmap = mpl.colormaps["Spectral"]
colors = base_cmap(np.linspace(0, 1, 256))[:, :3]

# Convert RGB to HSV
hsv = rgb_to_hsv(colors)

# Boost saturation
hsv[:, 1] = np.clip(hsv[:, 1] * 1.8, 0, 1)

# Brighten the overall colormap
gamma = 0.65
hsv[:, 2] = np.clip(hsv[:, 2] ** gamma, 0, 1)

# Darken the red end progressively
# Strongest effect at the darkest-red endpoint, fading toward orange
x = np.linspace(0, 1, 256)
red_darkening = 0.35 * np.exp(-((x / 0.12) ** 2))
hsv[:, 2] *= (1 - red_darkening)

# Convert back to RGB
vivid2_colors = hsv_to_rgb(hsv)

# Create custom colormap
cm_spectral_vivid2 = LinearSegmentedColormap.from_list(
    "spectral_vivid_dark",
    vivid2_colors,
    N=256
)

# Register colormap and reversed version
for cmap in (
    cm_spectral_vivid2,
    cm_spectral_vivid2.reversed(name="spectral_vivid_dark_r")
):
    if cmap.name not in mpl.colormaps:
        mpl.colormaps.register(cmap)
