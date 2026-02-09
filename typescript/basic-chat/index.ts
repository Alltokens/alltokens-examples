import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://api.alltokens.ru/api/v1",
});

async function main() {
  const completion = await client.chat.completions.create({
    model: "router",
    messages: [{ role: "user", content: "Write one sentence about routing." }],
  });

  console.log(completion.choices[0].message?.content);
}

main();
