import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY",
  baseURL: "https://api.alltokens.ru/api/v1",
});

async function main() {
  const embedding = await client.embeddings.create({
    model: "text-embedding-3-large",
    input: "Routing enables resilient AI systems.",
  });

  console.log(embedding.data[0].embedding.length);
}

main();
