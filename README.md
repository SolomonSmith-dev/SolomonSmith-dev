# Solomon Smith

Software engineer. I build LLM-backed features for products where a confident wrong answer costs more than no answer, and I write the tests that prove they refuse correctly. CS at CSUSB, graduating December 2026. Ten years in professional kitchens before this, dishwasher to head chef. Open to AI/ML and backend engineering roles starting January 2027.

## Now

**Founding Engineer, Recursa AI / [CourtRules](https://courtrules.app)** (Jul 2026 to present). Second engineer on a legal-data platform covering filing rules for 1,653 judges. Shipped the judge assistant: ask a filing question, get an answer quoting the judge's own filed order, deep-linked to the page. Every claim is verified verbatim against the source before it renders; if nothing survives, it refuses. Also: iCal/CSV court-calendar exports (RFC 5545/4180, CWE-1236 guard, 35 tests), query analytics ranking data gaps, the repo's first README.

## Projects

| Project | What it proves | Stack |
|---|---|---|
| [arda](https://github.com/SolomonSmith-dev/arda) | Multi-agent service: LangGraph orchestrator on native Anthropic tool_use, Redis executor, LlamaIndex RAG, MCP server. 425 tests run offline with no API keys. Deployed 24/7 on my own Debian host. | Python, FastAPI, LangGraph, Redis, Docker |
| [phishguard](https://github.com/SolomonSmith-dev/phishguard) | LightGBM URL classifier, test AUC 0.9943, 1.54% FPR on Tranco top-5000. Found and fixed dataset leakage; documented in LIMITATIONS.md. | Python, LightGBM, FastAPI, ONNX |
| [soc-triage-ai](https://github.com/SolomonSmith-dev/soc-triage-ai) | RAG alert triage with MITRE ATT&CK mapping, similarity guardrail, strict JSON schema. 7/7 harness. [3-min demo](https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9). | Python, Claude API, ChromaDB, Streamlit |
| [DocMind](https://github.com/SolomonSmith-dev/DocMind) | PDF Q&A with page-level citations, prompt-injection defense, rate limiting. 48 tests, CI. | Python, FastAPI, ChromaDB, Ollama |

## Open source

- [equinor/semeio#895](https://github.com/equinor/semeio/pull/895): fixed a pytest-console-scripts deprecation across the test suite.

[solomonsmith.dev](https://solomonsmith.dev) · [LinkedIn](https://www.linkedin.com/in/solomonsmithdev/) · solomonsmithdev@gmail.com
