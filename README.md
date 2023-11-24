# UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS
## FACULTAD DE INGENIERÍA

### CARRERA PROFESIONAL DE CIENCIAS DE LA COMPUTACIÓN


![Logo UPC](https://th.bing.com/th/id/OIP.uI-98YWzIvsuhXVyKRkv9gHaHk?pid=ImgDet&rs=1)
---

## Trabajo Parcial

**Alumnos**:
- Alcides Rommel Charapaqui Reluz - u202021294
- Llaguento de la Cruz, Marlon Omar - U20201B055
- Diego Humbser Meza - u202012711
- Quispe Ayala Diego Juan Pablo - U202020065

---

#### Machine Learning

**Profesor**:
- Canaval Sanchez, Luis Martin

---

#### CICLO 2023-02

---

### Preparación y Almacenamiento de Datos

**Objetivo**: Preparar el modelo 3D para su procesamiento y almacenarlo en un formato adecuado.

**Procedimiento**:
1. **Lectura del archivo STL**: Utilizamos la biblioteca `numpy-stl` para leer el archivo STL y obtener la malla 3D de la taza.
2. **División del Modelo**: El modelo 3D de la taza se dividió en dos partes, una representando la taza rota y la otra el fragmento sobrante.
3. **Almacenamiento**: Una vez procesado, se guardaron las dos partes en archivos STL separados para su posterior uso.

---

### Transformación de Datos para Modelos 3D

**Objetivo**: Convertir el modelo 3D a una representación adecuada para su uso en modelos de machine learning.

**Procedimiento**:
1. **Conversión a Voxels**: Convertimos el modelo 3D a una representación de voxel utilizando la herramienta `binvox`.
2. **Reducción de Dimensionalidad**: Se realizó una reducción de dimensionalidad en la representación de voxel para optimizar el procesamiento.
3. **Normalización**: Se normalizó la representación de voxel para asegurar que todos los valores estén en un rango estándar, típicamente entre 0 y 1.

---

### Conversión de Formato de Salida

**Objetivo**: Asegurarse de que el modelo 3D esté en un formato adecuado para la impresión.

**Procedimiento**:
- Dado que el formato STL es el formato requerido para la impresión 3D, no se necesitó ninguna conversión adicional.

---

![Diagrama](https://imgur.com/SS9nwjo)

