# Analizador-lexico

## Instalación y ejecución del analizador léxico

Este proyecto utiliza la librería **PLY** para construir el analizador léxico en Python. Antes de ejecutar el programa, es necesario instalar las dependencias correspondientes.

---

## 1. Instalar dependencias

Desde la terminal, dentro de la carpeta del proyecto, ejecuta:

```bash
pip install ply
```

En caso de usar Linux o macOS y tener varias versiones de Python instaladas, puede ser necesario usar:

```bash
pip3 install ply
```

---

## 2. Ejecutar el programa

El archivo principal del analizador debe ejecutarse desde la terminal.

Puede ejecutarse con el siguiente comando:

```bash
python analizador.py
```

En Linux o macOS, si el comando anterior no funciona, usar:

```bash
python3 analizador.py
```

---

## 3. Comandos por sistema operativo

### Windows

```bash
pip install ply
python analizador.py
```

### Linux

```bash
pip3 install ply
python3 analizador.py
```

### macOS

```bash
pip3 install ply
python3 analizador.py
```

---

## 4. Resultado esperado

Al ejecutar el programa, el analizador procesará el código de prueba incluido en el archivo y mostrará en la terminal los tokens reconocidos.

Ejemplo de salida:

```text
LexToken(INT,'int',2,5)
LexToken(ID,'main',2,9)
LexToken((,'(',2,13)
LexToken(),')',2,14)
LexToken({,'{',2,16)
LexToken(INT_CONST,5,4,65)
LexToken(;,';',4,66)
```

# Comparador de codigos

Revisar la documentación en: https://docs.google.com/document/d/1qQslshwdyPYu2UJb9Bc1FGjho8W4j5SKmo6SQtVQzBo/edit?tab=t.0#heading=h.w4l2uea0m447