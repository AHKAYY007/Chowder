export type UserIntent = {
  message: string;
  budget: number;
  health_goal: "healthy" | "cheap" | "anything";
  mode: "auto" | "assist";
  wallet_address: string;
};

export type AgentDecision = {
  selected_food_id: string;
  reason: string;
  rejected_user_choice?: string;
  confidence: number;
};

export type AgentResponse = {
  message: string;
  decision: AgentDecision;
  transaction_id?: string;
  created_at: string;
};
