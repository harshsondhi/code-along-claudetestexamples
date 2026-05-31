# Job Portal UI — Setup Notes

## Prerequisites

- Node.js 18+
- npm 9+

## Installation

```bash
npm install
```

## Development

```bash
npm run dev
```

Starts the Vite dev server at `http://localhost:5173`.

## Build

```bash
npm run build
```

Output is placed in `dist/`.

## Preview Production Build

```bash
npm run preview
```

## Linting

```bash
npm run lint
```

Uses ESLint flat config (`eslint.config.js`). Variables starting with uppercase or `_` are exempt from the `no-unused-vars` rule.

## Project Structure

```
src/
  context/       # Core contexts (Auth, Job, Theme)
  contexts/      # Data-fetching contexts (JobsData, Companies)
  data/          # Mock data (mockData.js)
  pages/         # Route-level components (admin/, employer/, job-seeker/)
  services/      # Simulated async API calls
  utils/         # Shared utilities (delay.js, etc.)
  App.jsx        # Root component with provider nesting and routes
```

## Environment

No `.env` file is required for local development. All data is mocked via `src/data/mockData.js` with localStorage persistence.

## Key localStorage Keys

| Key                        | Purpose                      |
| -------------------------- | ---------------------------- |
| `jobPortalUser`            | Authenticated user object    |
| `authToken`                | Session token                |
| `registeredUsers`          | All registered user accounts |
| `globalPostedJobs`         | Employer-posted jobs         |
| `jobApplications_{userId}` | Applications per user        |
| `savedJobs_{userId}`       | Saved jobs per user          |
| `postedJobs_{userId}`      | Jobs posted per employer     |

## User Roles

| Role              | Access                                 |
| ----------------- | -------------------------------------- |
| `ROLE_JOB_SEEKER` | Profile, applied jobs, saved jobs      |
| `ROLE_EMPLOYER`   | Post job, manage jobs, view applicants |
| `ROLE_ADMIN`      | Admin dashboard and admin pages        |
