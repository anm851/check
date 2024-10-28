
### `extract_rar.py`
Este script utiliza el módulo `rarfile` para extraer el archivo `.rar` protegido con contraseña.

```python
import rarfile

# Nombre del archivo .rar a extraer
rar_file_path = 'archivo_protegido.rar'
# Contraseña del archivo .rar
password = 'python123'

try:
    # Abre el archivo .rar usando el módulo rarfile
    with rarfile.RarFile(rar_file_path) as rf:
        # Extrae todos los archivos del .rar usando la contraseña
        rf.extractall(pwd=password)
    print("Archivo extraído correctamente.")
except rarfile.BadRarFile:
    print("Error: El archivo .rar está dañado o no es válido.")
except rarfile.RarWrongPassword:
    print("Error: La contraseña es incorrecta.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
