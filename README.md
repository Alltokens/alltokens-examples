# AllTokens Examples

Minimal, production-style examples for using **AllTokens** — a unified OpenAI-compatible gateway for 80+ providers and 400+ models.

These examples are intentionally small and copy-paste friendly so you can get a working request in under a minute.

## What is AllTokens?

AllTokens provides a single OpenAI-compatible API that lets you:

* route requests across multiple models
* avoid vendor lock-in
* optimize for cost, latency, or reliability
* operate LLM workloads as production infrastructure

API base:

```
https://api.alltokens.ru/api/v1
```

Docs:

```
https://alltokens.ru/docs
```

---

# Quick Start (30 seconds)

## Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.alltokens.ru/api/v1"
)

completion = client.chat.completions.create(
    model="router",
    messages=[{"role": "user", "content": "Say hello in one word"}]
)

print(completion.choices[0].message.content)
```

---

## TypeScript

```ts
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.ALLTOKENS_API_KEY,
  baseURL: "https://api.alltokens.ru/api/v1",
});

const completion = await client.chat.completions.create({
  model: "router",
  messages: [{ role: "user", content: "Hello" }],
});

console.log(completion.choices[0].message.content);
```

---

# Drop-in OpenAI Replacement

Already using OpenAI?

Change **one line**:

```
base_url → https://api.alltokens.ru/api/v1
```

No other migration required for most workloads.

See `/openai-replacement` for diffs.

---

# Examples

## Basic Chat

Minimal request using router mode.

## Streaming

Receive tokens as they are generated via SSE.

## Routing

Control cost / speed / reliability using routing metadata.

## Embeddings

Generate vectors using OpenAI-compatible endpoints.

---

# When to use router

Prefer:

```
model="router"
```

when you want automatic optimization across models and providers.

Use explicit models only when deterministic behavior is required.

---

# Docs

[https://alltokens.ru/docs](https://alltokens.ru/docs)
