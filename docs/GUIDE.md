# Guía del Lab (versión alumno)
## Objetivo
- Aprender a detectar secretos filtrados, auditar commits y mitigar correctamente.
- Subir el repo a GitHub (público) y activar seguridad gratuita.

## Pasos resumidos
1) `git init`, primer commit con contenido actual (incluye secretos falsos).
2) Buscar secretos con `grep` (y opcionalmente Gitleaks).
3) Ver historial y autoría (`git log`, `git blame`).
4) Mitigar: añadir `.env` a `.gitignore`, remover del índice (`git rm --cached`), documentar incidente.
5) Subir a GitHub y activar pestaña Security (Dependabot/Secret scanning para público).
