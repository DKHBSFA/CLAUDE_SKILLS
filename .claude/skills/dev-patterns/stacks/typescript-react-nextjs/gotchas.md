# Common Gotchas: TypeScript + React + Next.js

## 1. "use client" Directive Missing

**Problema:**
```typescript
// app/components/counter.tsx
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0); // Error!
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

**Errore:**
```
Error: useState only works in Client Components. Add the "use client" directive at the top of the file.
```

**Soluzione:**
```typescript
// app/components/counter.tsx
'use client'; // Add this at the top!

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

**Regola:** Se usi useState, useEffect, onClick, o qualsiasi hook/event handler, serve `'use client'`.

---

## 2. Async Component Without Await

**Problema:**
```typescript
// app/users/page.tsx
export default async function UsersPage() {
  const users = getUsers(); // Forgot await!

  return (
    <ul>
      {users.map(user => <li>{user.name}</li>)} {/* Error: users is a Promise */}
    </ul>
  );
}
```

**Errore:**
```
TypeError: users.map is not a function
```

**Soluzione:**
```typescript
export default async function UsersPage() {
  const users = await getUsers(); // Add await!

  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

---

## 3. Passing Server Components to Client Components

**Problema:**
```typescript
// This won't work as expected
'use client';

import { ServerComponent } from './server-component';

export function ClientWrapper() {
  return (
    <div>
      <ServerComponent /> {/* Can't import Server Component in Client Component */}
    </div>
  );
}
```

**Soluzione - Use Children Pattern:**
```typescript
// client-wrapper.tsx
'use client';

export function ClientWrapper({ children }: { children: React.ReactNode }) {
  return <div className="wrapper">{children}</div>;
}

// page.tsx (Server Component)
import { ClientWrapper } from './client-wrapper';
import { ServerComponent } from './server-component';

export default function Page() {
  return (
    <ClientWrapper>
      <ServerComponent /> {/* Pass as children instead */}
    </ClientWrapper>
  );
}
```

---

## 4. Hydration Mismatch

**Problema:**
```typescript
'use client';

export function DateDisplay() {
  // Different on server vs client!
  return <p>Today is {new Date().toLocaleString()}</p>;
}
```

**Errore:**
```
Hydration failed because the initial UI does not match what was rendered on the server.
```

**Soluzione:**
```typescript
'use client';

import { useState, useEffect } from 'react';

export function DateDisplay() {
  const [date, setDate] = useState<string | null>(null);

  useEffect(() => {
    setDate(new Date().toLocaleString());
  }, []);

  if (!date) return <p>Loading...</p>;
  return <p>Today is {date}</p>;
}
```

---

## 5. Fetch Cache Default Behavior

**Problema:**
```typescript
// This is cached indefinitely by default!
const data = await fetch('https://api.example.com/data');
```

**Soluzione:**
```typescript
// No cache
const data = await fetch('https://api.example.com/data', {
  cache: 'no-store'
});

// Revalidate every 60 seconds
const data = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 }
});

// Or set at page level
export const revalidate = 60; // seconds
```

---

## 6. Missing Key in Lists

**Problema:**
```typescript
{users.map(user => (
  <div>{user.name}</div> // Warning: Each child should have a unique "key" prop
))}
```

**Soluzione:**
```typescript
{users.map(user => (
  <div key={user.id}>{user.name}</div>
))}
```

**NON usare l'indice come key (tranne liste statiche):**
```typescript
// BAD - problemi con reordering/filtering
{users.map((user, index) => (
  <div key={index}>{user.name}</div>
))}

// GOOD
{users.map(user => (
  <div key={user.id}>{user.name}</div>
))}
```

---

## 7. useEffect Missing Dependencies

**Problema:**
```typescript
'use client';

function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId in deps!

  return <div>{user?.name}</div>;
}
```

**Warning:**
```
React Hook useEffect has a missing dependency: 'userId'.
```

**Soluzione:**
```typescript
useEffect(() => {
  fetchUser(userId).then(setUser);
}, [userId]); // Include all dependencies
```

---

## 8. Importing Server-Only Code in Client

**Problema:**
```typescript
// lib/db.ts
import { PrismaClient } from '@prisma/client';
export const db = new PrismaClient();

// components/user-list.tsx
'use client';
import { db } from '@/lib/db'; // Error! Can't use Prisma in client
```

**Soluzione - Use Server Actions:**
```typescript
// app/actions/users.ts
'use server';
import { db } from '@/lib/db';

export async function getUsers() {
  return db.user.findMany();
}

// components/user-list.tsx
'use client';
import { getUsers } from '@/app/actions/users';
import { useEffect, useState } from 'react';

export function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsers().then(setUsers);
  }, []);

  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

**Oppure usa `server-only`:**
```typescript
// lib/db.ts
import 'server-only'; // Throws error if imported in client
import { PrismaClient } from '@prisma/client';
export const db = new PrismaClient();
```

---

## 9. Router Methods in Server Components

**Problema:**
```typescript
// app/page.tsx (Server Component)
import { useRouter } from 'next/navigation';

export default function Page() {
  const router = useRouter(); // Error! Hooks can't be used in Server Components
  return <button onClick={() => router.push('/home')}>Go Home</button>;
}
```

**Soluzione:**
```typescript
// Option 1: Make it a Client Component
'use client';
import { useRouter } from 'next/navigation';

export default function Page() {
  const router = useRouter();
  return <button onClick={() => router.push('/home')}>Go Home</button>;
}

// Option 2: Use Link component (stays Server Component)
import Link from 'next/link';

export default function Page() {
  return <Link href="/home">Go Home</Link>;
}

// Option 3: Use redirect in Server Action
import { redirect } from 'next/navigation';

export default function Page() {
  async function handleAction() {
    'use server';
    redirect('/home');
  }
  return <form action={handleAction}><button>Go Home</button></form>;
}
```

---

## 10. TypeScript Strict Null Checks

**Problema:**
```typescript
interface User {
  id: string;
  name: string;
  email?: string;
}

function sendEmail(user: User) {
  // Error: Object is possibly 'undefined'
  console.log(user.email.toLowerCase());
}
```

**Soluzione:**
```typescript
function sendEmail(user: User) {
  // Option 1: Optional chaining
  console.log(user.email?.toLowerCase());

  // Option 2: Guard clause
  if (!user.email) return;
  console.log(user.email.toLowerCase());

  // Option 3: Non-null assertion (solo se sicuro al 100%)
  console.log(user.email!.toLowerCase());
}
```

---

## 11. Environment Variables in Client

**Problema:**
```typescript
'use client';

// This will be undefined!
const apiUrl = process.env.API_URL;
```

**Soluzione:**
```typescript
// Use NEXT_PUBLIC_ prefix for client-accessible env vars
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
```

**.env:**
```
# Server-only (safe for secrets)
DATABASE_URL=postgresql://...
API_SECRET=secret123

# Client-accessible (no secrets!)
NEXT_PUBLIC_API_URL=https://api.example.com
```

---

## 12. Circular Imports

**Problema:**
```typescript
// user.ts
import { Order } from './order';
export interface User {
  orders: Order[];
}

// order.ts
import { User } from './user';
export interface Order {
  user: User; // Circular!
}
```

**Soluzione:**
```typescript
// types/index.ts - Single source of truth
export interface User {
  id: string;
  name: string;
  orders: Order[];
}

export interface Order {
  id: string;
  userId: string;
  user?: User;
}
```

---

## 13. Form Reset After Server Action

**Problema:**
```typescript
export function CreateForm() {
  async function handleCreate(formData: FormData) {
    'use server';
    await createItem(formData);
    // Form doesn't reset!
  }

  return (
    <form action={handleCreate}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}
```

**Soluzione:**
```typescript
'use client';

import { useRef } from 'react';
import { createItem } from '@/app/actions';

export function CreateForm() {
  const formRef = useRef<HTMLFormElement>(null);

  async function handleSubmit(formData: FormData) {
    await createItem(formData);
    formRef.current?.reset();
  }

  return (
    <form ref={formRef} action={handleSubmit}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}
```

---

## 14. Dynamic Imports for Client Components

**Problema:**
```typescript
// Heavy chart library loads on initial page load
import { HeavyChart } from './heavy-chart';
```

**Soluzione:**
```typescript
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('./heavy-chart'), {
  loading: () => <p>Loading chart...</p>,
  ssr: false // If chart doesn't work server-side
});
```

---

## 15. Stale Closure in Callbacks

**Problema:**
```typescript
'use client';

function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setTimeout(() => {
      setCount(count + 1); // Uses stale `count`!
    }, 1000);
  };

  return <button onClick={handleClick}>{count}</button>;
}
```

**Soluzione:**
```typescript
const handleClick = () => {
  setTimeout(() => {
    setCount(c => c + 1); // Use callback form
  }, 1000);
};
```
