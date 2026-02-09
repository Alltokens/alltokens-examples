import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.ALLTOKENS_API_KEY,
  baseURL: process.env.ALLTOKENS_BASE_URL,
});

export async function POST(req: Request) {
  const { message } = await req.json();

  const completion = await client.chat.completions.create({
    model: "router",
    messages: [{ role: "user", content: message }],
  });

  return Response.json({
    response: completion.choices[0].message?.content,
  });
}
