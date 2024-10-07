# convert_yaml_to_md

Convierte los ficheros de yaml que estan en la carpeta docs a formato markdown en la carpeta md

## Explicación del Código

### Importación de Módulos:
- **os**: Para interactuar con el sistema de archivos.
- **yaml**: Para cargar y manipular archivos YAML.

### Función `yaml_to_markdown`:
- Abre y lee el archivo YAML.
- Convierte el contenido YAML a Markdown utilizando la función `convert_dict_to_markdown`.
- Escribe el contenido convertido en un archivo Markdown.

### Función `convert_dict_to_markdown`:
- Convierte recursivamente un diccionario en formato YAML a una cadena en formato Markdown.
- Utiliza encabezados (`#`, `##`, `###`, etc.) para representar la estructura jerárquica del YAML.
- Maneja listas y elementos simples adecuadamente.

### Función `convert_all_yaml_to_md`:
- Crea el directorio de salida si no existe.
- Itera sobre todos los archivos en el directorio especificado (`docs`).
- Convierte cada archivo YAML a un archivo Markdown con el mismo nombre.

### Punto de Entrada del Script:
- Llama a la función `convert_all_yaml_to_md` para iniciar el proceso de conversión.

Este script debería convertir correctamente los archivos YAML a Markdown, manteniendo la estructura y jerarquía del contenido.
