# Guía de estandarización de entornos

Objetivo: que cualquier intern deje listo su equipo en Windows, Linux o macOS con el mismo resultado, antes de empezar los micro-proyectos. En las primeras etapas no hace falta Docker; se usa Python puro con un entorno virtual.

## Requisitos comunes

- Python 3.10 o superior
- Git
- Un editor (VS Code recomendado)

## Windows (con WSL2)

1. Abre PowerShell como administrador y ejecuta `wsl --install`. Reinicia cuando lo pida y crea tu usuario de Ubuntu.
2. Abre la terminal de Ubuntu e instala lo necesario:

   ```bash
   sudo apt update && sudo apt install -y python3 python3-venv python3-pip git
   ```

3. Trabaja dentro del sistema de archivos de Linux (por ejemplo `~/proyectos`), no en `/mnt/c`: es más rápido y evita problemas de permisos.
4. En VS Code instala la extensión *WSL* y abre el proyecto con `code .` desde la terminal de Ubuntu.

## Linux (Debian/Ubuntu)

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git
```

En Fedora: `sudo dnf install -y python3 python3-pip git`.

## macOS

1. Instala Homebrew siguiendo las instrucciones de https://brew.sh.
2. Ejecuta:

   ```bash
   brew install python git
   ```

## Verificación

```bash
python3 --version
git --version
python3 -m venv .venv && source .venv/bin/activate
pip --version
```

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
| --- | --- | --- |
| `python` no se reconoce (Windows) | Se está usando PowerShell sin Python instalado | Usa la terminal de Ubuntu (WSL2) y el comando `python3`. |
| Error `pg_config executable not found` al instalar `psycopg2` | Falta compilar contra librerías de PostgreSQL | Instala `psycopg2-binary`, como indica el `requirements.txt` del micro-proyecto 1. |
| `SSL connection is required` al conectar a la base de datos | El servicio en la nube exige SSL | Agrega `?sslmode=require` a la `DATABASE_URL`. |
| `externally-managed-environment` al usar pip | El Python del sistema está protegido | Crea y activa un entorno virtual (`python3 -m venv .venv`). |
| Docker no ve WSL2 (más adelante, en el proyecto final) | La integración con WSL no está activada | En Docker Desktop: Settings > Resources > WSL integration, y activa tu distribución. |

## Cuándo se necesita Docker

Solo en el proyecto integrador final, donde se aplican los estándares EngX (Docker, GitHub Actions, JWT). Esta guía se ampliará con ese paso.
