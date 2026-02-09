## Replace OpenAI with AllTokens (TypeScript / JavaScript)

```diff
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
- baseURL: "https://api.openai.com/v1",
+ baseURL: "https://api.alltokens.ru/api/v1",
});
```

Drop-in compatible for most workloads.
