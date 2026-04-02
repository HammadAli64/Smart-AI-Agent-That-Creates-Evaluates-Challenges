# Smart AI Agent — Creates & Evaluates Challenges

Full-stack app where an **AI agent** generates personalized daily missions, **scores** written responses (points, timing, relevance), and powers a **Syndicate** dashboard with streaks, leaderboard, and bonus admin tasks.

**Repository:** [github.com/HammadAli64/Smart-AI-Agent-That-Creates-Evaluates-Challenges](https://github.com/HammadAli64/Smart-AI-Agent-That-Creates-Evaluates-Challenges)

## What it does

- **Daily missions** — OpenAI generates structured challenges by mood and category (business, money, fitness, power, grooming, personal).
- **Evaluation** — Submitted answers are scored server-side (word count, elapsed time, relevance, syndicate bonus).
- **Progress & sync** — Authenticated users persist dashboard state and **streak** data in the database (consecutive days with ≥1 completion; breaks after a missed day).
- **Leaderboard** — Points sync for ranked display.
- **Custom missions** — Users can add limited custom tasks per day; admins can assign bonus tasks with optional attachments.

## Tech stack

| Layer | Stack |
|--------|--------|
| API | **Django 4.2**, **Django REST Framework**, Token auth |
| AI | **OpenAI** (`OPENAI_MODEL`, default `gpt-4o-mini`) |
| UI | **Next.js** (App Router), **React**, **Tailwind CSS**, **Recharts** |

## Repository layout

```
production/
├── Backend/                 # Django project (syndicate_backend)
│   ├── api/                 # Mindset / OpenAI client, shared API routes
│   ├── apps/challenges/     # Challenges, scoring, referrals, admin tasks, progress
│   └── syndicate_backend/   # settings, urls
├── Frontend-Dashboard/        # Next.js app (Syndicate UI)
└── README.md
```

## Prerequisites

- **Python** 3.11+ (3.14+ supported with a small Django template workaround in settings)
- **Node.js** 20+ recommended
- **OpenAI API key**

## Backend setup

```bash
cd Backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Create `Backend/.env` (never commit real secrets):

```env
DJANGO_SECRET_KEY=your-secret-key
OPENAI_API_KEY=sk-...
# Optional:
# OPENAI_MODEL=gpt-4o-mini
```

```bash
python manage.py migrate
python manage.py createsuperuser   # optional, for admin
python manage.py runserver
```

API base (default): `http://127.0.0.1:8000/api/`

## Frontend setup

```bash
cd Frontend-Dashboard
npm install
```

Create `Frontend-Dashboard/.env.local`:

```env
NEXT_PUBLIC_SYNDICATE_API_URL=http://127.0.0.1:8000/api
```

```bash
npm run dev
```

App (default): `http://localhost:3000`

## Environment & security

- Keep **`.env`** / **`.env.local`** out of git (already in `.gitignore`).
- Use a strong **`DJANGO_SECRET_KEY`** in production and set **`DEBUG=False`** with proper **`ALLOWED_HOSTS`**, HTTPS, and CORS.

## License

Specify your license here (e.g. MIT) if you publish this repo publicly.

---

Built as a **Syndicate**-style productivity challenge system: AI creates missions, the API evaluates them, and the dashboard keeps users engaged with points and streaks.
