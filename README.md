# Finance Tracker

A Django web application for tracking personal transactions. Users register, sign in, and manage their own entries from a dashboard with a Tailwind CSS interface. PostgreSQL stores data; WhiteNoise serves static assets in production.

## Features

- **Authentication**: Registration, login, and logout (Django auth).
- **Transactions**: Create, read, update, and delete transactions; each row is scoped to the signed-in user.
- **Dashboard**: Total balance summary and a sortable-style table with edit/delete actions.
- **Categories**: Food, Rent, Salary, Entertainment, Misc.
- **Feedback**: Django messages for success and error states on forms and actions.
- **Admin**: Django admin for `Transaction` records (with `list_display` on key fields).

## Tech stack

| Area | Choice |
|------|--------|
| Framework | Django 5.2 |
| Database | PostgreSQL (`psycopg2-binary`) |
| Config | `python-dotenv` (`.env` for secrets and DB settings) |
| Static files (production) | WhiteNoise (`CompressedStaticFilesStorage`) |
| Frontend | Tailwind CSS (CDN), Inter font |

## Prerequisites

- Python 3.11+ (version used when the project was created)
- PostgreSQL server and a database the app can use

## Quick start

1. **Clone the repository** and enter the project directory.

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   ```

   On Windows (PowerShell):

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and set values (see table below). Generate a strong `SECRET_KEY` for any non-local use.

5. **Create the PostgreSQL database** (name should match `POSTGRES_DB` in `.env`).

6. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a user** (optional; for admin or testing login)

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the dashboard (login required). Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Environment variables

Defined in `.env` (not committed; listed in `.gitignore`). Example keys:

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Django secret key (required) |
| `DEBUG` | `True` / `False` (use `False` in production) |
| `POSTGRES_DB` | Database name |
| `POSTGRES_USER` | Database user |
| `POSTGRES_PASSWORD` | Database password |
| `POSTGRES_HOST` | Host (often `localhost`) |
| `POSTGRES_PORT` | Port (often `5432`) |

## URL map

| Path | Description |
|------|-------------|
| `/` | Transaction list (dashboard) |
| `/register/` | Sign up |
| `/add/` | New transaction |
| `/<id>/edit/` | Edit transaction |
| `/<id>/delete/` | Delete transaction |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout (POST) |
| `/admin/` | Django admin |

## Production notes

- Set `DEBUG=False`, a unique `SECRET_KEY`, and configure `ALLOWED_HOSTS` in `finance_tracker/settings.py` for your domain.
- Run `python manage.py collectstatic` so static files are collected into `STATIC_ROOT` for WhiteNoise.
- Use a proper WSGI/ASGI server (e.g. Gunicorn, uvicorn) behind a reverse proxy; do not rely on `runserver` in production.

## Project layout (high level)

- `finance_tracker/` — project settings and root URLconf.
- `expenses/` — `Transaction` model, views, forms, templates, and app URLs.
- `manage.py` — Django management entry point.

## License

No license file is included by default; add one if you distribute the project.
