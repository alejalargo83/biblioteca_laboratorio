# Importar un modulo que gestiona archivos .yaml
import yaml


def init_config():
    """Get configuration variables for the app"""

    # Ruta del archivo de configuración
    filepath = "config/config.yaml"

    config = None
    with open(filepath) as file_stream:
        config = yaml.full_load(file_stream)
    return config

# Variable global de configuración
config = init_config()
