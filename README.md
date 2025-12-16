# Ejercicios de Python - Guía de GitHub Copilot

Este repositorio contiene ejercicios de aprendizaje de Python. A continuación encontrarás una guía completa sobre cómo usar GitHub Copilot para mejorar tu experiencia de programación.

## ¿Qué es GitHub Copilot?

GitHub Copilot es un asistente de programación impulsado por inteligencia artificial que te ayuda a escribir código más rápido y con menos esfuerzo. Funciona como un programador virtual que:

- Completa automáticamente tu código
- Sugiere funciones y soluciones completas
- Te ayuda a aprender nuevos patrones de programación
- Responde preguntas sobre programación mediante chat
- Puede editar y mejorar tu código existente

## Requisitos Previos

- Una cuenta de GitHub
- Suscripción a GitHub Copilot (disponible para estudiantes de forma gratuita)
- Visual Studio Code u otro editor compatible

## Instalación de GitHub Copilot

### 1. Activar la Suscripción

1. Ve a [GitHub Copilot](https://github.com/features/copilot)
2. Haz clic en "Start free trial" o "Buy GitHub Copilot"
3. Si eres estudiante, solicita el [GitHub Student Developer Pack](https://education.github.com/pack) para acceso gratuito

### 2. Instalar la Extensión en Visual Studio Code

1. Abre Visual Studio Code
2. Ve a la pestaña de Extensiones (Ctrl+Shift+X o Cmd+Shift+X)
3. Busca "GitHub Copilot"
4. Instala las siguientes extensiones:
   - **GitHub Copilot** - Para completado de código
   - **GitHub Copilot Chat** - Para conversaciones con IA

5. Reinicia VS Code si es necesario
6. Inicia sesión con tu cuenta de GitHub cuando se te solicite

## Cómo Usar GitHub Copilot

### Autocompletado de Código

Mientras escribes código, Copilot sugerirá automáticamente completados:

1. **Comienza a escribir** - Copilot mostrará sugerencias en gris
2. **Acepta la sugerencia** - Presiona `Tab` para aceptar
3. **Ver alternativas** - Presiona `Alt+]` (siguiente) o `Alt+[` (anterior)
4. **Rechazar** - Presiona `Esc` o continúa escribiendo

**Ejemplo práctico:**
```python
# Escribe un comentario describiendo lo que quieres hacer
# calcular el promedio de una lista de números

# Copilot sugerirá automáticamente el código
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
```

### GitHub Copilot Chat

El chat te permite hacer preguntas y recibir ayuda en tiempo real:

1. **Abrir el chat** - Presiona `Ctrl+Shift+I` o haz clic en el ícono de chat
2. **Hacer una pregunta** - Escribe tu pregunta en lenguaje natural
3. **Recibir respuestas** - Copilot te dará explicaciones y código

**Ejemplos de preguntas útiles:**
- "¿Cómo puedo leer un archivo CSV en Python?"
- "Explica qué hace esta función"
- "¿Cómo manejo excepciones en Python?"
- "Ayúdame a optimizar este código"

### GitHub Copilot Edits (Agente de Copilot)

Esta es la característica más avanzada que funciona como un agente inteligente para editar tu código:

#### Abrir Copilot Edits

1. **Método 1:** Presiona `Ctrl+Shift+I` y luego haz clic en el ícono de "Edits"
2. **Método 2:** Usa el comando `GitHub Copilot: Open Copilot Edits`
3. **Método 3:** Selecciona código, clic derecho → "Copilot" → "Start in Editor"

#### Cómo Usar el Agente de Copilot

**Paso 1: Agrega archivos al contexto**
- Haz clic en "Add files" en el panel de Copilot Edits
- Selecciona los archivos que quieres que Copilot modifique
- Puedes agregar múltiples archivos a la vez

**Paso 2: Describe lo que quieres**
En el campo de texto, describe los cambios que necesitas:

```
Ejemplos de instrucciones:
- "Agrega comentarios explicativos a todas las funciones"
- "Convierte esta función para que use type hints"
- "Refactoriza este código para hacerlo más eficiente"
- "Agrega manejo de errores con try-except"
```

**Paso 3: Revisa y acepta cambios**
- Copilot mostrará los cambios propuestos
- Revisa cada cambio cuidadosamente
- Acepta o rechaza según tus necesidades
- Haz clic en "Accept" para aplicar los cambios

#### Comandos Especiales del Agente

Puedes usar comandos especiales con el prefijo `/`:

- `/explain` - Explica el código seleccionado
- `/fix` - Sugiere correcciones para errores
- `/tests` - Genera pruebas unitarias
- `/doc` - Genera documentación

## Ejemplos Prácticos para Este Repositorio

### Ejemplo 1: Mejorar el archivo somma.py

**Instrucción para Copilot Edits:**
```
Agrega type hints y mejora el manejo de errores en somma.py
```

**Resultado esperado:**
```python
def suma(valore_1: str, valore_2: str) -> int:
    try:
        v1 = int(valore_1)
        v2 = int(valore_2)
        somma_totale = v1 + v2
        return somma_totale
    except ValueError:
        print("Error: Por favor ingresa números válidos")
        return 0
```

### Ejemplo 2: Agregar Documentación

**Usando Chat:**
```
Agrega docstrings a todas las funciones en este archivo
```

### Ejemplo 3: Crear Nuevos Ejercicios

**En el chat, pregunta:**
```
Crea un ejercicio de Python para practicar bucles while
```

## Consejos y Mejores Prácticas

### ✅ Hacer

- **Sé específico** en tus instrucciones
- **Revisa siempre** el código generado antes de aceptarlo
- **Usa comentarios** para guiar a Copilot
- **Experimenta** con diferentes formulaciones de preguntas
- **Aprende** del código que Copilot genera

### ❌ Evitar

- No aceptes código sin entenderlo
- No dependas completamente de Copilot para aprender
- No compartas información sensible en el chat
- No uses Copilot para hacer trampa en tareas escolares

## Atajos de Teclado Útiles

| Acción | Windows/Linux | macOS |
|--------|--------------|-------|
| Aceptar sugerencia | `Tab` | `Tab` |
| Rechazar sugerencia | `Esc` | `Esc` |
| Siguiente sugerencia | `Alt+]` | `Option+]` |
| Sugerencia anterior | `Alt+[` | `Option+[` |
| Abrir Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Inline Chat | `Ctrl+I` | `Cmd+I` |

## Solución de Problemas

### Copilot no sugiere nada

1. Verifica que estés conectado a tu cuenta de GitHub
2. Revisa que la extensión esté habilitada
3. Asegúrate de tener una suscripción activa
4. Reinicia VS Code

### Las sugerencias no son relevantes

1. Escribe comentarios más descriptivos
2. Proporciona más contexto en tu código
3. Usa nombres de variables más claros
4. Divide problemas complejos en pasos más pequeños

### Error de autenticación

1. Cierra sesión y vuelve a iniciar sesión
2. Ve a Settings → GitHub → Sign out
3. Reinicia VS Code e inicia sesión nuevamente

## Recursos Adicionales

- [Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Copilot en VS Code](https://code.visualstudio.com/docs/editor/github-copilot)
- [Guía de inicio rápido](https://docs.github.com/en/copilot/quickstart)
- [Mejores prácticas](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

## Sobre Este Repositorio

Este repositorio contiene ejercicios básicos de Python para aprendizaje. Los archivos incluyen:

- `saluto.py` - Ejercicio de saludo básico
- `somma.py` - Suma de dos números
- `giorni.py` - Manejo de días de la semana
- `mesi.py` - Manejo de meses
- `massimo.py` - Encontrar el máximo
- `crivello.py` - Algoritmo del cribado
- Y más...

Usa GitHub Copilot para:
- Entender mejor cada ejercicio
- Mejorar el código existente
- Crear variaciones de los ejercicios
- Aprender nuevas técnicas de Python

## Preguntas Frecuentes

**P: ¿Es gratis GitHub Copilot?**
R: Hay una prueba gratuita. Los estudiantes verificados obtienen acceso gratuito con GitHub Student Developer Pack.

**P: ¿Funciona con Python?**
R: Sí, Copilot funciona excelentemente con Python y muchos otros lenguajes.

**P: ¿Necesito internet?**
R: Sí, Copilot requiere conexión a internet para funcionar.

**P: ¿Puedo usar Copilot en otros editores?**
R: Sí, está disponible para VS Code, Visual Studio, JetBrains IDEs, y Neovim.

---

**¡Feliz programación con GitHub Copilot! 🚀**

Si tienes preguntas o sugerencias, abre un issue en este repositorio.
