import os
import re

# CONFIGURACIÓN: 'PalabraOriginal': 'TuPalabra'
REEMPLAZOS = {
    'nomenclaturavieja': 'NomenclaturaNueva',
    'oldprojectname': 'MyCustomProject',
    '.claude': '.opencode',
    'claude code': 'opencode',
    'claude': 'opencode',
    'AskUserQuestion': 'Question',
    'paul:':'paul-',
    'paul-framework':'paul-framework-opencode'
}

def ejecutar_reemplazo():
    for root, dirs, files in os.walk("."):
        if ".git" in dirs: dirs.remove(".git")
        for file in files:
            if file == "transformar.py" or file.endswith(".yml"): continue
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                
                nuevas_lineas = []
                for linea in lineas:
                    # OBVIAR VERSIÓN: Si es el package.json y la línea tiene "version", no la tocamos
                    if file == "package.json" and '"version":' in linea:
                        nuevas_lineas.append(linea)
                        continue
                    
                    # Proceso de reemplazo normal
                    nueva_linea = linea
                    for viejo, nuevo in REEMPLAZOS.items():
                        insensible = re.compile(re.escape(viejo), re.IGNORECASE)
                        nueva_linea = insensible.sub(nuevo, nueva_linea)
                    nuevas_lineas.append(nueva_linea)
                
                nuevo_contenido = "".join(nuevas_lineas)
                original_contenido = "".join(lineas)

                if nuevo_contenido != original_contenido:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(nuevo_contenido)
            except: pass

if __name__ == "__main__":
    ejecutar_reemplazo()
