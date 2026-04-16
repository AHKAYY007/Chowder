import { UserIntent, AgentResponse } from "./types";

const apiBase = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export async function submitIntent(intent: UserIntent): Promise<AgentResponse> {
  const response = await fetch(`${apiBase}/intents/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(intent),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(errorText || "Failed to submit intent");
  }

  return response.json();
}
