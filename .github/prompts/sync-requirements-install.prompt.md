---
name: sync-requirements-install
description: Sincroniza el contenido del archivo install con los requerimientos del proyecto.
---
# Sincronizar requirements.txt → install.json

Quiero que sincronices automáticamente las dependencias entre requirements.txt e install.json en este proyecto comfyui-kpu-utils.

## Objetivo
Actualizar o crear el archivo `install.json` en la raíz del proyecto para que siempre refleje exactamente las dependencias listadas en `requirements.txt`.

## Instrucciones para el agente

1. Lee todas las dependencias actuales de `requirements.txt`.
2. Genera o actualiza `install.json` con este formato:

{
  "pip": [
    "paquete>=version",
    "paquete2>=version"
  ]
}

3. Si `install.json` ya existe, reemplaza únicamente su contenido para que coincida con `requirements.txt`.
4. No elimines, modifiques ni toques ningún otro archivo del proyecto.
5. Mantén el JSON ordenado, válido y con indentación estándar.
6. No añadas dependencias que no estén en `requirements.txt`.
7. Si una dependencia en `requirements.txt` no tiene versión, inclúyela tal cual.
8. Después de actualizar `install.json`, explícame brevemente:
   - Qué dependencias detectaste
   - Cómo las sincronizaste
   - Si hubo cambios respecto a la versión anterior

## Resultado esperado
Un archivo `install.json` perfectamente sincronizado con `requirements.txt`, listo para que ComfyUI instale automáticamente las dependencias cuando este nodo se coloque en `custom_nodes`.
