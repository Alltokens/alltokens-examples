curl https://api.alltokens.ru/api/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -N \
  -d '{
    "model": "router",
    "stream": true,
    "messages": [
      {"role": "user", "content": "Explain streaming briefly"}
    ]
  }'
