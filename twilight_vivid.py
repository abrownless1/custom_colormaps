# Modified version of matplotlib twilight_shifted colormap that is brighter 

import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, hsv_to_rgb, rgb_to_hsv

# Start with twilight_shifted
base_cmap = mpl.colormaps["twilight_shifted"]

# Sample the original colormap
colors = base_cmap(np.linspace(0, 1, 256))[:, :3]

# Convert RGB to HSV
hsv = rgb_to_hsv(colors)

# Increase saturation and slightly increase brightness
hsv[:, 1] = np.clip(hsv[:, 1] * 1.35, 0, 1)
hsv[:, 2] = np.clip(hsv[:, 2] * 1.12, 0, 1)

# Convert back to RGB
vivid_colors = hsv_to_rgb(hsv)

# Create custom colormap
cm_twilight_vivid = LinearSegmentedColormap.from_list(
    "twilight_vivid",
    vivid_colors,
    N=256
)

# Register colormap and reversed version
mpl.colormaps.register(cm_twilight_vivid)
mpl.colormaps.register(
    cm_twilight_vivid.reversed(name="twilight_vivid_r")
)
