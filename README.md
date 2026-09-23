# Personal Finance

An Odoo application to log personal money in and out — amount, currency, cash vs transfer — with chatter and archive.

![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)
![Odoo](https://img.shields.io/badge/Odoo-14--16-714B67.svg)
![Python](https://img.shields.io/badge/Python-3-blue.svg)
![Version](https://img.shields.io/badge/module-1.0.0-informational.svg)

![Personal Finance module icon](static/description/icon.png)

From `__manifest__.py`:

| Key | Value |
| --- | --- |
| `name` | Personal Finance |
| `summary` | Centralize your finances |
| `version` | 1.0.0 |
| `license` | LGPL-3 |
| `depends` | `base`, `mail` |
| `application` | True |

The manifest does **not** pin an Odoo series (`14.0.x` / `16.0.x`). Views use classic `<tree>` (renamed to `<list>` in Odoo 17+), so this module matches **Odoo 14–16**.

## Why

Odoo already does company accounting. This module is a smaller personal ledger: one form per movement, filters for income vs expense, and mail tracking when a line changes.

## Features

Exact surface from `models/`, `views/`, and `security/`:

- **`finances.entry`** — date, note (`name`), integer amount, currency (`CUP`, `MLC`, `USD`, `BTC`), transaction type (`Efectivo` / `Transferencia`), flow (`Entrada` / `Salida`), starred flag, archive (`active`)
- **Mail chatter** on entries (`mail.thread` + `mail.activity.mixin`) so field changes are tracked
- **List / form / search**: filters for income, expense, starred, archived; left **searchpanel** grouped by type
- **Window action** also exposes kanban, pivot, and activity views
- **`finances.journal`** — stub journal line with a `Many2one` to an entry (tree/form/search exist; the tree has no columns yet)
- **Menus** (Spanish UI strings): *Finanzas Personales* → *Administracion de Entradas* → *Registro* and *Diario*
- **ACL**: internal users (`base.group_user`) can read/write/create/unlink both models

## How it works

```
  Finanzas Personales
  └── Administracion de Entradas
        ├── Registro  →  finances.entry   (the real ledger)
        └── Diario    →  finances.journal (Many2one → entry)
```

An entry is a single movement. Changing tracked fields posts a chatter message. Archiving sets `active = False` (standard Odoo archive). The journal model is a placeholder for grouping lines later.

## Quickstart

Odoo is not started in this workspace. Install on an Odoo 14–16 instance:

1. Copy this folder into your addons path as **`personal_finance`**.
   Access rules reference `personal_finance.model_finances_entry` and
   `personal_finance.model_finances_journal`, so the **directory name must be
   `personal_finance`**, not the GitHub repo name.
2. Add that path to `addons_path` and restart Odoo.
3. Enable **Developer Mode** → *Apps* → **Update Apps List**.
4. Search **Personal Finance** and **Install**.
5. Open the *Finanzas Personales* app and create a *Registro*.

No extra config settings are shipped. Currencies and transaction labels are selections on the entry form.

## Project structure

```
.
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── finances_entry.py
│   └── finances_journal.py
├── views/
│   ├── menu.xml
│   ├── entry_view.xml
│   └── journal_view.xml
├── security/
│   └── ir.model.access.csv
└── static/description/icon.png
```

## Limitations

- Manifest `description` is still `To do...`.
- `finances.journal` does not compute balances or list child entries.
- Amount is an **integer**, not `Monetary`; there is no running balance or report.
- UI strings are mostly Spanish; model names are English.
- Access XML IDs assume the technical module name `personal_finance`.
- Not tested on Odoo 17+ (`<tree>` vs `<list>`).

## License

LGPL-3, as declared in `__manifest__.py`. See [LICENSE](LICENSE).
