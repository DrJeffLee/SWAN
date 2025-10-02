import numpy as np
import matplotlib.pyplot as plt

# Tank dimensions
TANK_LENGTH = 16.8  # m
TANK_WIDTH = 12.0   # m
DX = 0.05  # X grid spacing
DY = 0.05  # Y grid spacing

# X positions and corresponding depth values
x_values_original = np.array([0.0, 4.8, 7.2, 14.96, 16.8])  
z_values_original = np.array([0.3, 0.35, 0.4, 0.45, 0.5])  

# Generate fine grid
x_values_fine = np.arange(0, TANK_LENGTH + DX, DX)
y_values_fine = np.arange(0, TANK_WIDTH + DY, DY)

# Interpolate depth values
z_values_fine = np.interp(x_values_fine, x_values_original, z_values_original)

# Create meshgrid
NY, NX = len(y_values_fine), len(x_values_fine)

def create_coastal_bathymetry(z_values_fine, NY, NX, coast_width=1):
    """
    Create bathymetry with gradual depth reduction near boundaries
    
    Parameters:
    - z_values_fine: Interpolated depth values along X
    - NY: Number of Y grid points
    - NX: Number of X grid points
    - coast_width: Width of coastal transition zone (m)
    """
    # Initialize bathymetry grid
    bathymetry = np.zeros((NY, NX))
    
    # Coastal boundary treatment zones
    coast_points_y = int(coast_width / DY)
    coast_points_x = int(coast_width / DX)
    
    # Create full depth profile for mid tank region
    for j in range(NY):
        # Apply linear tapering at top and bottom boundaries
        if j < coast_points_y or j >= (NY - coast_points_y):
            # Taper depth near Y boundaries
            y_taper_factor = min(j, NY - j - 1) / coast_points_y
            bathymetry[j, :] = z_values_fine * y_taper_factor
        else:
            # Full depth in mid region
            bathymetry[j, :] = z_values_fine
    
    # Taper depth near left (west) boundary
    bathymetry[:, :coast_points_x] *= np.linspace(0, 1, coast_points_x)
    
    return bathymetry

# Generate bathymetry with coastal boundaries
bathymetry = create_coastal_bathymetry(z_values_fine, NY, NX)

# SWAN bathymetry file
filename = "swan_bathymetry_coastal.dat"

# Write bathymetry file
with open(filename, "w") as f:
    # Write header
    #f.write("SWAN BATHYMETRY FILE - WITH COASTAL BOUNDARIES\n")
    #f.write(f"Number of X points: {NX}\n")
    #f.write(f"Number of Y points: {NY}\n")
    #f.write(f"X origin: 0.0 m\n")
    #f.write(f"Y origin: 0.0 m\n")
    #f.write(f"X spacing (DX): {DX} m\n")
    #f.write(f"Y spacing (DY): {DY} m\n")
   # f.write("\n")  # Blank line before data
   
    # Write bathymetry values 
    for i in range(NY):
        row_depths = [f"{max(0, abs(depth)):.4f}" for depth in bathymetry[i]]
        f.write(" ".join(row_depths) + "\n")

print(f"Coastal bathymetry file '{filename}' generated successfully.")

# Visualization
plt.figure(figsize=(18, 12))

# 2D Bathymetry Contour Plot
plt.subplot(221)
plt.imshow(bathymetry, aspect='auto', cmap='viridis', 
           extent=[0, TANK_LENGTH, 0, TANK_WIDTH])  # Origin at bottom-left
plt.colorbar(label='Depth (m)')
plt.title('Bathymetry with Coastal Boundaries')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')

# Length (X-axis) Cross-section Plot
plt.subplot(222)
mid_width_index = NY // 2
plt.plot(x_values_fine, -bathymetry[mid_width_index, :], label='X-axis Cross-section')
plt.title(f'Depth Profile Along Length\n(at Y = {y_values_fine[mid_width_index]:.2f} m)')
plt.xlabel('X Position (m)')
plt.ylabel('Depth (m)')
plt.grid(True)
plt.legend()

# Width (Y-axis) Cross-section Plot
plt.subplot(223)
mid_length_index = NX // 2
plt.plot(y_values_fine, -bathymetry[:, mid_length_index], label='Y-axis Cross-section')
plt.title(f'Depth Profile Along Width\n(at X = {x_values_fine[mid_length_index]:.2f} m)')
plt.xlabel('Y Position (m)')
plt.ylabel('Depth (m)')
plt.grid(True)
plt.legend()

# Boundary Conditions Explanation
plt.subplot(224)
plt.text(0.5, 0.5, 
    "Boundary Conditions:\n"
    "- Left boundary: Gradual depth reduction\n"
    "- Top/Bottom boundaries: Linear depth taper\n"
    "- Maintains original sloped profile\n"
    f"Coastal transition width: 0.5 m",
    horizontalalignment='center', 
    verticalalignment='center', 
    bbox=dict(facecolor='white', alpha=0.7))
plt.axis('off')
plt.title('Boundary Condition Summary')

plt.tight_layout()
plt.show()