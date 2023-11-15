import os
import pyvista as pv
import numpy as np

input_folder = "train_stl"
output_folder = "train_images"

os.makedirs(output_folder, exist_ok=True)

# Función para convertir STL a PNG
def stl_to_png(stl_file, output_folder):
    # Leer el archivo STL
    mesh = pv.read(stl_file)
    
    # Configurar el plotter para renderizado fuera de pantalla
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(mesh, color="white")  # Asumiendo que el color blanco es adecuado
    
    # Definir vectores de vista para capturar diferentes ángulos del vaso
    view_vectors = [
        (1, 0, 0),   # Vista lateral
        (0, 1, 0),   # Vista frontal
        (-1, 0, 0),  # Vista lateral opuesta
        (0, -1, 0),  # Vista trasera
        (0, 0, 1)    # Vista superior
    ]
    
    # Recorrer cada vector de vista y guardar la captura de pantalla
    for view_vector in view_vectors:

        plotter.view_vector(view_vector)
        
        file_name = f"{os.path.splitext(os.path.basename(stl_file))[0]}_{view_vector}.png"
        
        plotter.screenshot(os.path.join(output_folder, file_name))

stl_file_name = 'beker1.stl'


stl_path = os.path.join(input_folder, stl_file_name)

stl_to_png(stl_path, output_folder)
