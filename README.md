# 🧮 Calculadora en Python — Práctica de Git Avanzado

Proyecto simple de calculadora con operaciones básicas, usado 
para practicar comandos avanzados de Git.

## ⚙️ Funcionalidades
- Sumar
- Restar
- Multiplicar
- Dividir (valida división por cero)
- Potencia
- Raíz cuadrada (valida números negativos)
- Porcentaje

## 📝 Cómo ejecutar
```
python calculadora.py
```

---

## 📚 Teoría — Comandos que vas a usar

### git commit --amend
Modifica el ÚLTIMO commit que hiciste (cambia su mensaje y/o 
agrega archivos que olvidaste). No crea un commit nuevo, corrige 
el anterior.
```
git commit --amend -m "nuevo mensaje"
```

### git reset
Deshace commits. `HEAD~1` significa "un commit atrás del actual" 
(`HEAD~2` serían dos atrás, etc.)

Tiene 3 tipos:
- `--soft`: deshace el commit, pero tus cambios siguen listos 
  para volver a commitear
- `--mixed` (el que se usa si no escribes nada): deshace el 
  commit y el "add", los cambios quedan en tus archivos sin preparar
- `--hard`: borra TODO, incluso los cambios en tus archivos 
  (¡cuidado, esto no se puede deshacer!)

```
git reset --soft HEAD~1
```

---

## 🎯 Tu tarea

### Paso 1 — Configurar tu identidad
```
git config user.name "Tu Nombre"
git config user.email "tu-correo"
```

### Paso 2 — Explorar el historial
```
git log --oneline
```

### Paso 3 — Corregir el ÚLTIMO commit con amend
```
git commit --amend -m "docs: agregar instrucciones del proyecto"
```

### Paso 4 — Practicar reset
```
git reset --soft HEAD~1
git commit -m "docs: agregar instrucciones del proyecto"
```

### Paso 5 — Nuevos commits (conventional commits)
Se agregaron las siguientes mejoras al proyecto:
1. Función `dividir` con validación de división por cero
2. Docstrings en todas las funciones
3. Funciones `potencia`, `raiz_cuadrada` y `porcentaje`

### Paso 6 — Subir a tu repositorio
```
git push -u origin main
```
### Investigación adicional
Ejecuta git reflog. En tu README.md, en una sección 
"Investigación adicional", explica en 2-3 líneas qué información 
muestra este comando.

## 🔍 Investigación adicional
El comando `git reflog` muestra el historial completo de movimientos 
de HEAD (commits, amends, resets, checkouts, etc.), incluso aquellos 
que ya no son visibles con `git log`. Es útil para recuperar commits 
o cambios que parecían "perdidos" después de un `reset --hard` u 
otras operaciones destructivas.

## ✅ Entrega
Link de tu repositorio (fork) + pantallazo de "git log --oneline"
