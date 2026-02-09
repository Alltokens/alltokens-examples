import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://api.alltokens.ru/api/v1",
});

async function main() {
  const completion = await client.chat.completions.create({
    model: "router",
    messages: [{ role: "user", content: "Why avoid vendor lock-in?" }],
    extra_body: {
      metadata: {
        objective: "fastest",
      },
    },
  });

  console.log(completion.choices[0].message?.content);
}

main();
