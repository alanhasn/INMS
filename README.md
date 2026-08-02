# Internal Network Management System (INMS)

A Django web application for institutions (companies, schools) to manage their internal network: devices, events, reports, and role-based user access.

See [prd.md](prd.md) for the full project brief.

## Features

| Area                                                                        | Status                              |
| --------------------------------------------------------------------------- | ----------------------------------- |
| Auth (register/login/logout/password reset), profile                        | Working                             |
| Role-based access control (Admin / Manager / Employee)                      | Working                             |
| Device management (create/read/update/delete)                               | Working                             |
| Event logging (auto-logged on device changes and login/logout/failed login) | Working                             |
| Reports (generation, CSV/PDF export)                                        | Not implemented yet -- listing only |
| REST API                                                                    | Scaffolding only, no live endpoints |
| Automated tests                                                             | Not written yet                     |

## Technology Stack

- Backend: Django 5, Django REST Framework, Simple JWT
- Database: SQLite (development), PostgreSQL (production)
- Auth: Django's built-in auth + Google OAuth2 (`social-auth`)
- Frontend: Django templates, Tailwind CSS, vanilla JavaScript

## Installation

Prerequisites:

- Python 3.10+
- pip

Steps:

1. Clone the repository:
   ```
   git clone https://github.com/alanhasn/INMS.git
   cd INMS
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create your local environment file:
   ```
   cp .env.example .env
   ```

   Then fill in `.env` with real values -- see [.env.example](.env.example) for what each
   variable is for. At minimum, for local development you need:- `DJANGO_SETTINGS_MODULE=config.settings.dev`
   - `DJANGO_SECRET_KEY` -- generate one with:
     ```
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
   - `client_id` / `client_secret` (Google OAuth2 -- required even if you don't use social login; see note below)
   - `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` (used for password reset emails)
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

   New users default to the `Employee` role. To use an Admin/Manager account, set
   `role` on your superuser via `/admin/` after creating it.
7. Run the development server:
   ```
   python manage.py runserver
   ```

> **Note:** `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY`/`SECRET` are read unconditionally at
> settings-import time (`config/settings/base.py`), so `client_id`/`client_secret`
> must be set in `.env` even if you don't intend to use Google login yet -- any
> placeholder string works for that case.

## Database notes

- Local development uses SQLite by default (no separate DB server required).
  `config/settings/dev.py` points `DATABASES` at `db.sqlite3` in the project root.
- Production is expected to use PostgreSQL. Configure the connection with the
  environment variables `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and
  `DB_PORT` (read in `config/settings/prod.py`).

## Usage

- Access the application at http://localhost:8000
- Use the admin panel at http://localhost:8000/admin
- Login with the superuser credentials created during installation

## Deploying

`config/settings/prod.py` sets `DEBUG = False` and reads `ALLOWED_HOSTS` (comma-separated)
plus HTTPS-related security settings from the environment -- see
[.env.example](.env.example). Before deploying, run:

```
python manage.py check --deploy
```

and resolve anything it flags.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up your dev environment,
coding conventions, and how to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contact

For any questions or suggestions, please open an issue or contact:

- Email:  vorsynth1987@gmail.com
- GitHub: https://github.com/alanhasn
