import os  # Módulo para interactuar con el sistema operativo
import yaml  # Módulo para trabajar con archivos YAML

# Función para convertir un archivo YAML a Markdown
def yaml_to_markdown(yaml_file, markdown_file):
    # Abre el archivo YAML y carga su contenido
    with open(yaml_file, 'r', encoding='utf-8') as yf:
        data = yaml.safe_load(yf)
    
    # Convierte el contenido del diccionario YAML a formato Markdown
    md_content = convert_dict_to_markdown(data)
    
    # Escribe el contenido Markdown en el archivo de salida
    with open(markdown_file, 'w', encoding='utf-8') as mf:
        mf.write(md_content)

# Función recursiva para convertir un diccionario a formato Markdown
def convert_dict_to_markdown(data, level=1):
    md_lines = []  # Lista para almacenar las líneas de Markdown
    for key, value in data.items():
        if isinstance(value, dict):
            # Si el valor es un diccionario, crea un encabezado y llama recursivamente
            md_lines.append(f"{'#' * level} {key}")
            md_lines.append(convert_dict_to_markdown(value, level + 1))
        elif isinstance(value, list):
            # Si el valor es una lista, crea un encabezado y procesa cada elemento
            md_lines.append(f"{'#' * level} {key}")
            for item in value:
                if isinstance(item, dict):
                    md_lines.append(convert_dict_to_markdown(item, level + 1))
                else:
                    md_lines.append(f"- {item}")
        else:
            # Si el valor es un elemento simple, lo añade como una línea de lista
            md_lines.append(f"- **{key}**: {value}")
    return '\n'.join(md_lines)  # Une todas las líneas en una sola cadena

# Función para convertir todos los archivos YAML en un directorio a Markdown
def convert_all_yaml_to_md(yaml_dir='docs', md_dir='md'):
    # Crea el directorio de salida si no existe
    if not os.path.exists(md_dir):
        os.makedirs(md_dir)
    
    # Itera sobre todos los archivos en el directorio YAML
    for filename in os.listdir(yaml_dir):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            yaml_file = os.path.join(yaml_dir, filename) # Ruta completa del archivo YAML
            base_filename = filename.replace('.yaml', '.md') # Cambiamos lña extensión del archivo de destino
            markdown_file = os.path.join(md_dir, base_filename) # Ruta completa del archivo Markdown
            yaml_to_markdown(yaml_file, markdown_file) # Convierte el archivo YAML a Markdown
            print(f'Converted {yaml_file} to {markdown_file}') # Imprime un mensaje de confirmación

# Punto de entrada del script
if __name__ == '__main__':
    convert_all_yaml_to_md() # Llama a la función principal para convertir los archivos
