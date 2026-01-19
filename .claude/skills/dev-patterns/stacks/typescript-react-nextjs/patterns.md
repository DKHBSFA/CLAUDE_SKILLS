# Stack Patterns: TypeScript + React + Next.js

**Generated:** 2026-01-19
**Stack:** TypeScript + React 18+ + Next.js 14+ (App Router)

---

## TypeScript Idioms

### Naming Conventions
- **Files:** `kebab-case.ts` for utilities, `PascalCase.tsx` for components
- **Variables/Functions:** `camelCase`
- **Types/Interfaces:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Components:** `PascalCase`

### Type Definitions

```typescript
// Prefer interfaces for object shapes
interface User {
  id: string;
  name: string;
  email: string;
}

// Use type for unions, intersections, utilities
type Status = 'pending' | 'active' | 'inactive';
type UserWithRole = User & { role: string };

// Avoid `any` - use `unknown` for truly unknown types
function parseJson(json: string): unknown {
  return JSON.parse(json);
}

// Use generics for reusable types
interface ApiResponse<T> {
  data: T;
  error: string | null;
}
```

### Strict Type Patterns

```typescript
// Use const assertions for literal types
const ROLES = ['admin', 'user', 'guest'] as const;
type Role = typeof ROLES[number]; // 'admin' | 'user' | 'guest'

// Discriminated unions for state management
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

// Type guards
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'email' in value
  );
}
```

---

## Next.js App Router Patterns

### Project Structure

```
app/
├── (auth)/                 # Route group (no URL segment)
│   ├── login/
│   │   └── page.tsx
│   └── register/
│       └── page.tsx
├── (dashboard)/
│   ├── layout.tsx          # Shared layout for dashboard
│   └── settings/
│       └── page.tsx
├── api/                    # API routes
│   └── users/
│       └── route.ts
├── layout.tsx              # Root layout
├── page.tsx                # Home page
├── error.tsx               # Error boundary
├── loading.tsx             # Loading UI
└── not-found.tsx           # 404 page
components/
├── ui/                     # Reusable UI components
│   ├── button.tsx
│   └── input.tsx
├── features/               # Feature-specific components
│   └── user/
│       ├── user-card.tsx
│       └── user-list.tsx
└── layouts/                # Layout components
    └── header.tsx
lib/
├── db.ts                   # Database client
├── auth.ts                 # Auth utilities
└── utils.ts                # General utilities
types/
└── index.ts                # Shared types
```

### Server Components (Default)

```typescript
// app/users/page.tsx - Server Component
import { getUsers } from '@/lib/db';

export default async function UsersPage() {
  // Direct database/API access - runs on server only
  const users = await getUsers();

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### Client Components

```typescript
// components/ui/counter.tsx - Client Component
'use client';

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}
```

### When to Use Client Components
- Event handlers (onClick, onChange)
- useState, useEffect, useReducer
- Browser APIs (localStorage, window)
- Custom hooks using state/effects
- Third-party libraries requiring client

---

## Data Fetching

### Server-Side Fetching (Recommended)

```typescript
// app/users/[id]/page.tsx
interface PageProps {
  params: { id: string };
}

export default async function UserPage({ params }: PageProps) {
  const user = await fetch(`${process.env.API_URL}/users/${params.id}`, {
    next: { revalidate: 60 } // Revalidate every 60 seconds
  }).then(res => res.json());

  return <UserProfile user={user} />;
}

// Generate static params for static generation
export async function generateStaticParams() {
  const users = await getUsers();
  return users.map(user => ({ id: user.id }));
}
```

### Parallel Data Fetching

```typescript
export default async function DashboardPage() {
  // Parallel fetching - much faster than sequential
  const [user, orders, notifications] = await Promise.all([
    getUser(),
    getOrders(),
    getNotifications()
  ]);

  return (
    <Dashboard
      user={user}
      orders={orders}
      notifications={notifications}
    />
  );
}
```

### Client-Side Fetching (When Needed)

```typescript
'use client';

import useSWR from 'swr';

const fetcher = (url: string) => fetch(url).then(res => res.json());

export function UserOrders({ userId }: { userId: string }) {
  const { data, error, isLoading } = useSWR(
    `/api/users/${userId}/orders`,
    fetcher
  );

  if (isLoading) return <Skeleton />;
  if (error) return <Error message={error.message} />;

  return <OrderList orders={data} />;
}
```

---

## API Routes

### Route Handlers

```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const page = searchParams.get('page') ?? '1';

  const users = await getUsers({ page: parseInt(page) });

  return NextResponse.json({ data: users });
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const user = await createUser(body);

    return NextResponse.json({ data: user }, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 400 }
    );
  }
}
```

### Dynamic Route Handlers

```typescript
// app/api/users/[id]/route.ts
interface RouteParams {
  params: { id: string };
}

export async function GET(request: NextRequest, { params }: RouteParams) {
  const user = await getUserById(params.id);

  if (!user) {
    return NextResponse.json(
      { error: 'User not found' },
      { status: 404 }
    );
  }

  return NextResponse.json({ data: user });
}
```

---

## React Patterns

### Component Props

```typescript
// Explicit props interface
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  children,
  onClick
}: ButtonProps) {
  return (
    <button
      className={cn(variants[variant], sizes[size])}
      onClick={onClick}
      disabled={isLoading}
    >
      {isLoading ? <Spinner /> : children}
    </button>
  );
}
```

### Composition Pattern

```typescript
// Compound components
interface CardProps {
  children: React.ReactNode;
}

function Card({ children }: CardProps) {
  return <div className="card">{children}</div>;
}

Card.Header = function CardHeader({ children }: CardProps) {
  return <div className="card-header">{children}</div>;
};

Card.Body = function CardBody({ children }: CardProps) {
  return <div className="card-body">{children}</div>;
};

// Usage
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
</Card>
```

### Custom Hooks

```typescript
// hooks/use-local-storage.ts
'use client';

import { useState, useEffect } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(initialValue);

  useEffect(() => {
    const item = window.localStorage.getItem(key);
    if (item) {
      setStoredValue(JSON.parse(item));
    }
  }, [key]);

  const setValue = (value: T | ((val: T) => T)) => {
    const valueToStore = value instanceof Function ? value(storedValue) : value;
    setStoredValue(valueToStore);
    window.localStorage.setItem(key, JSON.stringify(valueToStore));
  };

  return [storedValue, setValue] as const;
}
```

---

## State Management

### React Context (Simple State)

```typescript
// contexts/user-context.tsx
'use client';

import { createContext, useContext, useState, ReactNode } from 'react';

interface User {
  id: string;
  name: string;
}

interface UserContextType {
  user: User | null;
  setUser: (user: User | null) => void;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

export function UserProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within UserProvider');
  }
  return context;
}
```

### Zustand (Complex State)

```typescript
// stores/cart-store.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  id: string;
  quantity: number;
}

interface CartStore {
  items: CartItem[];
  addItem: (id: string) => void;
  removeItem: (id: string) => void;
  clearCart: () => void;
}

export const useCartStore = create<CartStore>()(
  persist(
    (set) => ({
      items: [],
      addItem: (id) =>
        set((state) => {
          const existing = state.items.find(item => item.id === id);
          if (existing) {
            return {
              items: state.items.map(item =>
                item.id === id
                  ? { ...item, quantity: item.quantity + 1 }
                  : item
              )
            };
          }
          return { items: [...state.items, { id, quantity: 1 }] };
        }),
      removeItem: (id) =>
        set((state) => ({
          items: state.items.filter(item => item.id !== id)
        })),
      clearCart: () => set({ items: [] })
    }),
    { name: 'cart-storage' }
  )
);
```

---

## Error Handling

### Error Boundaries

```typescript
// app/error.tsx
'use client';

interface ErrorProps {
  error: Error & { digest?: string };
  reset: () => void;
}

export default function Error({ error, reset }: ErrorProps) {
  return (
    <div className="error-container">
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

### API Error Handling

```typescript
// lib/api.ts
class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
    public code?: string
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

async function fetchApi<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(url, options);

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new ApiError(
      error.message ?? 'An error occurred',
      response.status,
      error.code
    );
  }

  return response.json();
}
```

---

## Form Handling

### React Hook Form + Zod

```typescript
// components/features/user/user-form.tsx
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email address'),
  age: z.number().min(18, 'Must be at least 18')
});

type UserFormData = z.infer<typeof userSchema>;

export function UserForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm<UserFormData>({
    resolver: zodResolver(userSchema)
  });

  const onSubmit = async (data: UserFormData) => {
    await createUser(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('name')} />
      {errors.name && <span>{errors.name.message}</span>}

      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}

      <input type="number" {...register('age', { valueAsNumber: true })} />
      {errors.age && <span>{errors.age.message}</span>}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Saving...' : 'Save'}
      </button>
    </form>
  );
}
```

---

## Server Actions (Next.js 14+)

```typescript
// app/actions/user.ts
'use server';

import { revalidatePath } from 'next/cache';
import { z } from 'zod';

const createUserSchema = z.object({
  name: z.string().min(2),
  email: z.string().email()
});

export async function createUser(formData: FormData) {
  const rawData = {
    name: formData.get('name'),
    email: formData.get('email')
  };

  const validatedData = createUserSchema.parse(rawData);

  await db.user.create({ data: validatedData });

  revalidatePath('/users');
}
```

```typescript
// Usage in component
export function CreateUserForm() {
  return (
    <form action={createUser}>
      <input name="name" required />
      <input name="email" type="email" required />
      <button type="submit">Create</button>
    </form>
  );
}
```
