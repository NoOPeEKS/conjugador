#/bin/sh
cd web/
mkdir -p /var/log/conjugador/
uv run gunicorn web_search:app -b 0.0.0.0:8000 --error-logfile /var/log/conjugador/gnuicorn.log --workers=2
