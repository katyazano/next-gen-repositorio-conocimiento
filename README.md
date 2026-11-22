# Repositorio de conocimiento Next Gen (Fase 2)

Repositorio colaborativo con resúmenes de los workshops, guías de configuración y plantillas de micro-proyectos del programa Next Gen. Nace de dos objetivos del proyecto de mejora continua:

- **Objetivo 1:** que los interns lleguen al proyecto final con práctica real, mediante dos micro-proyectos terminados antes del 19 de julio.
- **Objetivo 2:** tener material de consulta rápido de todos los workshops, publicado el 19 de julio.

## Estructura

| Carpeta | Contenido |
| --- | --- |
| `plantillas/` | Plantilla estándar de resumen de workshop (3 puntos clave, 2 comandos, 1 diagrama). |
| `resumenes/` | Un archivo por workshop, con el nombre `AAAA-MM-DD-tema.md`. Incluye el índice. |
| `guias/` | Guía de estandarización de entornos para Windows (WSL2), Linux y macOS. |
| `micro-proyectos/` | Micro-proyecto 1 (Python + base de datos en la nube) y micro-proyecto 2 (servicio en la nube + IA). |
| `.github/workflows/` | CI con GitHub Actions: lint y pruebas automáticas. |

## Cómo usarlo

1. Lee primero la [guía de entornos](guias/estandarizacion-entornos.md) y deja tu equipo listo.
2. Antes de ver una grabación completa, busca su resumen en [`resumenes/`](resumenes/README.md). Debería tomarte entre 15 y 20 minutos.
3. Haz cada micro-proyecto al terminar su bloque de cursos, no al final del programa.

## Cómo contribuir un resumen

1. Copia [`plantillas/resumen-workshop.md`](plantillas/resumen-workshop.md) a `resumenes/` con el nombre `AAAA-MM-DD-tema.md`.
2. Completa los tres puntos clave, los dos comandos y el diagrama. No pegues transcripciones ni credenciales.
3. Agrega tu resumen al índice de `resumenes/README.md`.
4. Abre un pull request y pide revisión a otro intern o a un mentor.

## Seguridad

Nunca subas archivos `.env`, llaves ni contraseñas. Lee el resumen [Manejo seguro de variables de entorno](resumenes/2026-07-10-variables-de-entorno.md) antes de tu primer commit con servicios en la nube.

## Medición

El KPI 2 (tiempo para extraer lo clave de un workshop) se sigue con las vistas y clones del repositorio, disponibles en la pestaña *Insights > Traffic* de GitHub para quien tenga permisos de escritura.
