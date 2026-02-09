Next.js + AllTokens starter

Minimal Next.js App Router project using AllTokens from a server API route.

This starter shows:
- how to call AllTokens from a Next.js backend
- how to expose a simple /api/chat endpoint

Requirements:
- Node.js 18+

Setup:

cd starters/nextjs-alltokens
npm install
cp .env.local.example .env.local

Set ALLTOKENS_API_KEY in .env.local.

Run:

npm run dev

Test:

curl http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
