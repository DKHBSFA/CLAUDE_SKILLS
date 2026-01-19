# CLI Commands: TypeScript + React + Next.js

## Package Management

### npm
| Action | Command |
|--------|---------|
| Install all dependencies | `npm install` |
| Add dependency | `npm install package-name` |
| Add dev dependency | `npm install -D package-name` |
| Remove dependency | `npm uninstall package-name` |
| Update all | `npm update` |
| Audit vulnerabilities | `npm audit` |
| Fix vulnerabilities | `npm audit fix` |

### pnpm (Recommended)
| Action | Command |
|--------|---------|
| Install all dependencies | `pnpm install` |
| Add dependency | `pnpm add package-name` |
| Add dev dependency | `pnpm add -D package-name` |
| Remove dependency | `pnpm remove package-name` |
| Update all | `pnpm update` |

### yarn
| Action | Command |
|--------|---------|
| Install all dependencies | `yarn` |
| Add dependency | `yarn add package-name` |
| Add dev dependency | `yarn add -D package-name` |
| Remove dependency | `yarn remove package-name` |
| Update all | `yarn upgrade` |

---

## Development

| Action | Command |
|--------|---------|
| Start dev server | `npm run dev` |
| Start with turbo | `npm run dev -- --turbo` |
| Start on custom port | `npm run dev -- -p 3001` |
| Build for production | `npm run build` |
| Start production server | `npm run start` |
| Export static site | `npm run build && npx next export` |

---

## TypeScript

| Action | Command |
|--------|---------|
| Type check (no emit) | `npx tsc --noEmit` |
| Type check watch mode | `npx tsc --noEmit --watch` |
| Generate declaration files | `npx tsc --declaration --emitDeclarationOnly` |
| Check specific files | `npx tsc --noEmit src/file.ts` |

---

## Linting & Formatting

### ESLint
| Action | Command |
|--------|---------|
| Lint all files | `npm run lint` |
| Lint with auto-fix | `npm run lint -- --fix` |
| Lint specific directory | `npx eslint src/` |
| Lint specific files | `npx eslint "src/**/*.{ts,tsx}"` |

### Prettier
| Action | Command |
|--------|---------|
| Format all files | `npx prettier --write .` |
| Check formatting | `npx prettier --check .` |
| Format specific files | `npx prettier --write "src/**/*.{ts,tsx}"` |

### Combined
```bash
# Lint then format
npm run lint -- --fix && npx prettier --write .
```

---

## Testing

### Vitest
| Action | Command |
|--------|---------|
| Run all tests | `npm run test` |
| Run in watch mode | `npm run test -- --watch` |
| Run single file | `npm run test -- src/file.test.ts` |
| Run with coverage | `npm run test -- --coverage` |
| Run UI mode | `npm run test -- --ui` |
| Update snapshots | `npm run test -- -u` |

### Jest (Alternative)
| Action | Command |
|--------|---------|
| Run all tests | `npm run test` |
| Run in watch mode | `npm run test -- --watch` |
| Run single file | `npm run test -- src/file.test.ts` |
| Run with coverage | `npm run test -- --coverage` |
| Run matching pattern | `npm run test -- -t "pattern"` |
| Update snapshots | `npm run test -- -u` |

### Playwright (E2E)
| Action | Command |
|--------|---------|
| Run all E2E tests | `npx playwright test` |
| Run with UI | `npx playwright test --ui` |
| Run headed | `npx playwright test --headed` |
| Run specific file | `npx playwright test tests/file.spec.ts` |
| Generate tests | `npx playwright codegen localhost:3000` |
| Show report | `npx playwright show-report` |

---

## Database (Prisma)

| Action | Command |
|--------|---------|
| Generate client | `npx prisma generate` |
| Create migration | `npx prisma migrate dev --name migration-name` |
| Apply migrations (prod) | `npx prisma migrate deploy` |
| Reset database | `npx prisma migrate reset` |
| Push schema (no migration) | `npx prisma db push` |
| Open Prisma Studio | `npx prisma studio` |
| Seed database | `npx prisma db seed` |
| Format schema | `npx prisma format` |

### Quick Database Commands
```bash
# Full reset and seed
npx prisma migrate reset

# Update after schema change (dev)
npx prisma migrate dev

# After pulling from git
npx prisma generate
```

---

## Code Generation

| Action | Command |
|--------|---------|
| Create component | Manual or use plop |
| Generate API types | `npx openapi-typescript schema.json -o types/api.ts` |
| Generate GraphQL types | `npx graphql-codegen` |

### Next.js Built-in
```bash
# Create new app
npx create-next-app@latest my-app

# With specific options
npx create-next-app@latest my-app --typescript --tailwind --eslint --app --src-dir
```

---

## Environment

| Action | Command |
|--------|---------|
| Check env vars | `npx next info` |
| Validate env | `npx dotenv -e .env -- node -e "console.log(process.env)"` |

### Environment Files Priority
```
.env                 # All environments
.env.local           # Local overrides (gitignored)
.env.development     # Development only
.env.production      # Production only
.env.test            # Test only
```

---

## Build Analysis

| Action | Command |
|--------|---------|
| Analyze bundle | `ANALYZE=true npm run build` |
| Check bundle size | `npx next build && npx next-bundle-analyzer` |

### Setup for analyze
```javascript
// next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
});

module.exports = withBundleAnalyzer({ /* config */ });
```

---

## Deployment

### Vercel
| Action | Command |
|--------|---------|
| Deploy | `npx vercel` |
| Deploy to production | `npx vercel --prod` |
| List deployments | `npx vercel ls` |
| Environment variables | `npx vercel env` |

### Docker
```bash
# Build image
docker build -t my-app .

# Run container
docker run -p 3000:3000 my-app

# Run with env file
docker run --env-file .env.production -p 3000:3000 my-app
```

---

## Debugging

| Action | Command |
|--------|---------|
| Start with debugger | `NODE_OPTIONS='--inspect' npm run dev` |
| Debug tests | `node --inspect-brk node_modules/.bin/jest --runInBand` |
| Check Next.js info | `npx next info` |

### VS Code Debug Config
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug server-side",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev"
    },
    {
      "name": "Next.js: debug client-side",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    }
  ]
}
```

---

## Cleaning

| Action | Command |
|--------|---------|
| Clean Next.js cache | `rm -rf .next` |
| Clean node_modules | `rm -rf node_modules` |
| Clean all caches | `rm -rf .next node_modules .turbo` |
| Fresh install | `rm -rf node_modules .next && npm install` |

---

## Common Workflows

### Morning Setup
```bash
git pull
npm install
npx prisma generate
npm run dev
```

### Before Commit
```bash
npm run lint -- --fix
npx tsc --noEmit
npm run test
```

### Before PR
```bash
npm run lint -- --fix
npx tsc --noEmit
npm run test
npm run build
```

### After Merge
```bash
git pull
npm install
npx prisma migrate dev
npm run dev
```
