import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://api.alltokens.ru/api/v1",
});

async function main() {
  const stream = await client.chat.completions.create({
    model: "router",
    messages: [{ role: "user", content: "Explain provider fallback briefly." }],
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta?.content;
    if (delta) process.stdout.write(delta);
  }
}

main();
