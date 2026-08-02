# Contributing to INMS

Thanks for considering a contribution. This document covers how the project
is laid out, how to set up your environment, and how to submit changes.

## Setup

Follow the [Installation](README.md#installation) section of the README first.
You'll need a working `.env` (copied from `.env.example`) before anything --
`manage.py` and the app both fail fast at import time if required variables
are missing.

## Project layout

Each Django app under `apps/` (`users`, `devices`, `events`, `reports`)
follows the same internal structure:

```
apps/<app>/
  models/       # one file per model, re-exported from __init__.py
  views/        # ui.py (server-rendered pages) and api.py (DRF, if any)
  urls/         # ui_urls.py and api_urls.py, mirroring views/
  forms.py      # ModelForms for the ui views
  permissions/  # role_required decorator usage / custom permission logic
  signals/      # signal receivers, wired via the app's apps.py ready()
  serializers/  # DRF serializers
  services/     # business logic that doesn't belong in a view
  tests/        # test_models.py, test_serializers.py, test_views.py
  templates/<app>/
```

Only `apps.users` currently has working `api.py`/serializers; the other
apps' API layers are unwired stubs. Templates that extend the dashboard
shell (`templates/base.html`) live in each app's own `templates/<app>/`
directory; shared partials (sidebar, top nav, modals) live in
`templates/partials/`.

## Conventions

- **Role checks**: use the `role_required(*roles)` decorator from
  `apps.users.permissions.user_permissions` on any view that should be
  restricted by `CustomUser.Roles` (`ADMIN`, `Manager`, `Employee`). It
  also enforces login, so don't stack it with `@login_required`.
- **Signals**: a new signal receiver module needs to be imported from its
  app's `AppConfig.ready()` (see `apps/events/apps.py`) or it will silently
  never fire -- Django doesn't auto-discover signal files.
- **Migrations**: run `makemigrations` per-app (e.g. `python manage.py
  makemigrations devices`) rather than a bare `makemigrations`, so you don't
  accidentally pick up unrelated model drift. `apps/*/migrations/*.py`
  (other than `__init__.py`) are gitignored by default in this repo but are
  force-added when they exist -- if you add a new migration, check
  `git status --ignored` and `git add -f` it if it doesn't show up under a
  normal `git add`.
- **Settings**: never hardcode a secret or credential in `config/settings/*.py`.
  Add it to `.env.example` (with a placeholder) and read it via
  `decouple.config(...)` with no default for anything sensitive.

## Before opening a PR

- Run `python manage.py check` (and `python manage.py check --deploy`
  against `config.settings.prod` if you touched settings).
- If you changed a model, make sure the migration is committed (see above).
- There's no test suite yet (`apps/*/tests/*.py` are all empty) -- if you're
  adding a non-trivial feature, adding tests for it is very welcome, even
  though the existing code doesn't have any to follow as a pattern yet.
- Manually exercise the page/flow you changed; several existing bugs in this
  project were UI wiring that looked right but silently didn't work (e.g. a
  form posting fields that didn't match the model).

## Commit messages

Write the *why*, not just the *what* -- e.g. "Fix device status badge always
showing Warning" plus a short body explaining the actual bug, not "update
devices.html". Keep unrelated changes in separate commits.

## Pull requests

1. Fork the repository (or branch directly if you have write access).
2. Create a branch: `git checkout -b feature/short-description` (or `fix/...`).
3. Commit your changes with a clear message (see above).
4. Push and open a PR against `main`. Describe what changed and how you
   tested it.
