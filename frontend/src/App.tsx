import { FormEvent, useState } from "react";
import { ethers } from "ethers";
import { submitIntent } from "./api";
import { AgentResponse, UserIntent } from "./types";
import { KITE_LOGGER_ADDRESS, KITE_LOGGER_ABI } from "./constants";

const defaultIntent: UserIntent = {
  message: "Find a healthy lunch under $15",
  budget: 15,
  health_goal: "healthy",
  mode: "auto",
  wallet_address: "",
};

function App() {
  const [intent, setIntent] = useState<UserIntent>(defaultIntent);
  const [response, setResponse] = useState<AgentResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [walletAddress, setWalletAddress] = useState<string | null>(null);
  const [provider, setProvider] = useState<ethers.BrowserProvider | null>(null);

  const connectWallet = async () => {
    if (!window.ethereum) {
      setError("MetaMask not installed");
      return;
    }
    try {
      const provider = new ethers.BrowserProvider(window.ethereum);
      await provider.send("eth_requestAccounts", []);
      const signer = await provider.getSigner();
      const address = await signer.getAddress();
      setWalletAddress(address);
      setProvider(provider);
      setIntent((prev) => ({ ...prev, wallet_address: address }));
      setError(null);
    } catch (err) {
      setError("Failed to connect wallet");
    }
  };

  const authorizeAgent = async () => {
    if (!provider || !walletAddress) return;
    try {
      const signer = await provider.getSigner();
      const contract = new ethers.Contract(KITE_LOGGER_ADDRESS, KITE_LOGGER_ABI, signer);
      // Assume agent address is known, perhaps from backend
      const agentAddress = "0xAgentAddressHere"; // Replace with actual
      const tx = await contract.authorizeAgent(agentAddress);
      await tx.wait();
      alert("Agent authorized!");
    } catch (err) {
      setError("Failed to authorize agent");
    }
  };

  const handleChange = (field: keyof Omit<UserIntent, "wallet_address">, value: string | number) => {
    setIntent((current) => ({
      ...current,
      [field]: value,
    }));
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();    if (!walletAddress) {
      setError("Please connect your wallet first");
      return;
    }    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const result = await submitIntent(intent);
      setResponse(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <header>
        <h1>Chowder</h1>
        <p>Autonomous food decision AI with on-chain logging.</p>
        {!walletAddress ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected: {walletAddress}</p>
            <button onClick={authorizeAgent}>Authorize Agent</button>
          </div>
        )}
      </header>

      <main>
        <section className="control-panel">
          <form onSubmit={handleSubmit}>
            <label>
              Request
              <textarea
                value={intent.message}
                onChange={(event) => handleChange("message", event.target.value)}
                rows={4}
              />
            </label>

            <div className="field-row">
              <label>
                Budget
                <input
                  type="number"
                  min={1}
                  value={intent.budget}
                  onChange={(event) => handleChange("budget", Number(event.target.value))}
                />
              </label>

              <label>
                Health goal
                <select
                  value={intent.health_goal}
                  onChange={(event) => handleChange("health_goal", event.target.value)}
                >
                  <option value="healthy">Healthy</option>
                  <option value="cheap">Cheap</option>
                  <option value="anything">Anything</option>
                </select>
              </label>

              <label>
                Mode
                <select value={intent.mode} onChange={(event) => handleChange("mode", event.target.value)}>
                  <option value="auto">Auto</option>
                  <option value="assist">Assist</option>
                </select>
              </label>
            </div>

            <button type="submit" disabled={loading || !walletAddress}>
              {loading ? "Submitting..." : "Submit Intent"}
            </button>
          </form>

          {error ? <div className="error-box">{error}</div> : null}
        </section>

        {response ? (
          <section className="response-panel">
            <h2>Agent Response</h2>
            <div className="card">
              <p className="response-message">{response.message}</p>
              <div className="response-meta">
                <strong>Decision ID:</strong> {response.decision.selected_food_id}
              </div>
              <div className="response-meta">
                <strong>Reason:</strong> {response.decision.reason}
              </div>
              <div className="response-meta">
                <strong>Confidence:</strong> {(response.decision.confidence * 100).toFixed(0)}%
              </div>
              {response.transaction_id ? (
                <div className="response-meta">
                  <strong>Transaction:</strong> {response.transaction_id}
                </div>
              ) : null}
              <div className="response-meta">
                <strong>Created:</strong> {new Date(response.created_at).toLocaleString()}
              </div>
            </div>
          </section>
        ) : null}
      </main>
    </div>
  );
}

export default App;
