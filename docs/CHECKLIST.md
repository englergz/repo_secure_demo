# Checklist de Seguridad del Repo
- [ ] `.gitignore` protege: `.env`, `*.pem`, `*.key`, `*.pfx`, `*.jks`, `*.keystore`
- [ ] Reviso `git diff` antes de commit
- [ ] Busco secretos con `grep` (o Gitleaks)
- [ ] Repo público: activé Security > secret scanning / Dependabot
- [ ] Documenté incidentes en README o Issues
