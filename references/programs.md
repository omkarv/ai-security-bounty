# Target Bounty Programs

## Tier 1: High payout, AI-focused scope

| Program | Scope | Payout Range | AI/GenAI Targets | URL |
|---------|-------|-------------|------------------|-----|
| Google VRP | Google products inc. Gemini, Cloud AI, Android AI features | $100 - $250,000+ | Gemini API, Vertex AI, Bard/Gemini app, AI Overviews | https://bughunters.google.com |
| OpenAI | ChatGPT, API, plugins, DALL-E, platform | $200 - $20,000+ | ChatGPT, API, plugins, function calling, code interpreter | https://bugcrowd.com/openai |
| Microsoft (MSRC) | Azure AI, Copilot, Bing AI, Office AI features | $500 - $250,000+ | Copilot, Azure OpenAI Service, Bing Chat | https://msrc.microsoft.com/bounty |
| Meta | Facebook, Instagram, WhatsApp, Llama-related infra | $500 - $300,000 | Llama deployment infra, Meta AI assistant | https://www.facebook.com/whitehat |
| Anthropic | Claude API and products | Undisclosed / case-by-case | Claude API, tool use, system prompts | https://www.anthropic.com (check disclosure policy) |

## Tier 2: Mid-size, growing AI surface

| Program | Scope | Payout Range | AI/GenAI Targets | URL |
|---------|-------|-------------|------------------|-----|
| HuggingFace | Hub, Spaces, Inference API, Transformers | Community recognition + case-by-case | Model hosting, Spaces sandboxing, Inference endpoints | https://huggingface.co/security |
| Mistral | API, La Plateforme | TBD (new program) | Chat API, fine-tuning endpoints | Check website |
| Cohere | API, Command, Embed, Rerank | Case-by-case | API auth, data handling, model endpoints | Check website |
| Stability AI | API, DreamStudio | Case-by-case | Image generation API, auth, data leakage | Check website |

## Tier 3: Broader scope with AI components

| Program | Scope | Payout Range | Notes |
|---------|-------|-------------|-------|
| GitHub (via MSRC) | Copilot, Actions, Codespaces | $500 - $30,000+ | Copilot code suggestions, Copilot Chat |
| Cloudflare | Workers AI, AI Gateway | $200 - $3,000+ | AI inference at edge |
| Vercel | v0, AI SDK | Case-by-case | AI-assisted code generation |
| Snap | My AI (Snapchat) | $500 - $30,000 | Chatbot safety, data leakage |

## Common AI vulnerability classes to target

1. **Prompt injection** — manipulating model behaviour via crafted inputs
2. **Data leakage** — extracting training data, system prompts, or PII via model outputs
3. **Auth/access control bypass** — accessing model endpoints, admin APIs, or other users' data
4. **SSRF via tool use** — abusing function calling / tool use to hit internal services
5. **Insecure deserialization** — model loading (pickle, safetensors bypass), plugin execution
6. **Rate limiting / resource exhaustion** — denial of service via expensive model calls
7. **Supply chain** — compromised model weights, poisoned dependencies, malicious plugins
8. **Sandbox escape** — breaking out of code execution environments (code interpreter, Spaces, etc.)
