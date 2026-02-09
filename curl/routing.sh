curl https://api.alltokens.ru/api/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "router",
    "messages": [
      {"role": "user", "content": "Why is routing useful?"}
    ],
    "metadata": {
      "objective": "balanced"
    }
  }'
