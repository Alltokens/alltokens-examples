## Replace OpenAI with AllTokens (Python)

Change one line:

```diff
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
-   base_url="https://api.openai.com/v1"
+   base_url="https://api.alltokens.ru/api/v1"
)
```

Most applications require no other changes.
