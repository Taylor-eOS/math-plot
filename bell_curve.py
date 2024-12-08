import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range and normal distribution parameters
x = np.linspace(-4, 4, 500)
mu = 0       # Mean
sigma = 1    # Standard deviation
y = norm.pdf(x, mu, sigma)  # Probability density function for the normal distribution

# Identify points for the flat tangent (at mean) and inflection point (at mu + sigma)
flat_tangent_x = mu
flat_tangent_y = norm.pdf(flat_tangent_x, mu, sigma)

inflection_x = mu + sigma
inflection_y = norm.pdf(inflection_x, mu, sigma)

# Slope of the tangent at the inflection point
slope_inflection = -inflection_x / (sigma**2) * inflection_y  # First derivative at inflection point

# Define tangent lines
flat_tangent = flat_tangent_y + 0 * (x - flat_tangent_x)  # Horizontal line
inflection_tangent = inflection_y + slope_inflection * (x - inflection_x)  # Tangent at inflection

# Plot the bell curve and tangents
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Bell Curve (Normal Distribution)", color="blue")
plt.axvline(flat_tangent_x, color="gray", linestyle="--", alpha=0.7, label="Mean (µ)")
plt.plot(x, flat_tangent, 'r--', label="Flat Tangent at µ")
plt.plot(x, inflection_tangent, 'g--', label="Tangent at Inflection Point (µ + σ)")
plt.scatter([flat_tangent_x, inflection_x], [flat_tangent_y, inflection_y], 
            color=["red", "green"], zorder=5, label="Key Points")

# Add labels and legend
plt.title("Bell Curve with Key Tangents")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

