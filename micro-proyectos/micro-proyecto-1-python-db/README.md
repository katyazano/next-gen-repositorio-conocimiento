# Micro-proyecto 1: conexión lógica y datos

**Ventana:** 06 al 15 de junio · **Esfuerzo máximo:** 2 a 3 días · **Responsable:** cada intern

## Objetivo

Construir un script de Python que se conecte a una base de datos PostgreSQL gratuita en la nube (independiente del sistema operativo) y haga un CRUD básico.

## Qué entregas

- Script que crea una tabla, inserta, lista, actualiza y elimina registros.
- Credenciales fuera del código, con `.env` y `.env.example`.
- Un resumen en `resumenes/` sobre lo que más te costó.

## Pasos

1. Crea una instancia PostgreSQL gratuita en la nube (por ejemplo Neon, Supabase o AWS RDS con Free Tier; verifica las condiciones vigentes). Esto suma aproximadamente 1 día de configuración.
2. Copia `.env.example` a `.env` y pega tu `DATABASE_URL`.
3. Crea el entorno virtual e instala dependencias:

   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Ejecuta el script:

   ```bash
   python main.py
   ```

## Criterios de logro

- [ ] El script funciona en tu sistema operativo siguiendo la guía de entornos.
- [ ] Ninguna credencial está en el historial de git.
- [ ] Las consultas usan parámetros (`%s`) y no concatenan texto.
