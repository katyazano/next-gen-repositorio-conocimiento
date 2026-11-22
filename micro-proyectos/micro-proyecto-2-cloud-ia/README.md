# Micro-proyecto 2: integración Cloud e IA

**Ventana:** 06 al 19 de julio · **Esfuerzo máximo:** 2 a 3 días · **Responsable:** cada intern

## Objetivo

Reutilizar la lógica del micro-proyecto 1 dentro de un servicio web (FastAPI), desplegarlo en un servicio de nube gratuito y manejar las credenciales de forma segura con variables de entorno.

## Qué entregas

- API con `GET /health` y un CRUD básico de tareas conectado a PostgreSQL.
- Variables de entorno configuradas en el servicio de nube, no en el código.
- Una función de IA generativa (`app/ia.py`) usando la herramienta que se vio en el curso de Gen AI.
- Pruebas que pasan en GitHub Actions.

## Pasos

1. Configura el entorno como en la [guía de entornos](../../guias/estandarizacion-entornos.md).
2. Copia `.env.example` a `.env`, instala dependencias y levanta la API:

   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. Ejecuta las pruebas:

   ```bash
   pytest -q
   ```

4. Despliega en el servicio de nube que indique el programa (por ejemplo AWS Free Tier) y carga las variables desde su panel de configuración. Revisa el límite de gasto antes de crear recursos.

## Criterios de logro

- [ ] `GET /health` responde `{"status": "ok"}`.
- [ ] No hay secretos en el código ni en el historial de git.
- [ ] La función de IA está implementada y documentada.
- [ ] El workflow de CI pasa en verde.
