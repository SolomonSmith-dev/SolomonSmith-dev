# Solomon Smith

AI/Backend Engineer. I build LLM-backed features for products where a confident wrong answer costs more than no answer, and I write the tests that prove they refuse correctly. CS at CSUSB, graduating December 2026. Ten years in professional kitchens before this, dishwasher to head chef. Open to AI/ML and backend engineering roles starting January 2027.

## Now

**Founding Engineer, Recursa AI / [CourtRules](https://courtrules.app)** (Jul 2026 to present). Second engineer on a legal-data platform covering filing rules for 1,653 judges. Shipped the judge assistant: ask a filing question, get an answer quoting the judge's own filed order, deep-linked to the page. Every claim is verified verbatim against the source before it renders; if nothing survives, it refuses. Also: iCal/CSV court-calendar exports (RFC 5545/4180, CWE-1236 guard, 35 tests), query analytics ranking data gaps, the repo's first README.

## Projects

Every number below is reproduced by a command in that repo's README.

| Project | What it proves | Evidence | Stack |
|---|---|---|---|
| [arda](https://github.com/SolomonSmith-dev/arda) | Multi-agent service: LangGraph orchestrator on native Anthropic tool_use, shell executor, LlamaIndex RAG, MCP server. Labelled injection evals show where the offline router leaks, and a demo mode closes the gap structurally. | 577 tests pass offline with no API keys; CI gates on eval drift | Python, FastAPI, LangGraph, Redis, Docker |
| [soc-triage-ai](https://github.com/SolomonSmith-dev/soc-triage-ai) | RAG alert triage with MITRE ATT&CK mapping and a fixed refusal when retrieval finds nothing. [3-min demo](https://www.loom.com/share/5ae859759c7e4036a5c73b251164e3e9). | 100-case harness replayed in CI, 109 tests, refusal precision 1.0 | Python, Claude API, ChromaDB, Streamlit |
| [sentinel](https://github.com/SolomonSmith-dev/sentinel) | Home-network security monitor I run on my own LAN: C++ libpcap sensor, Suricata, isolation-forest anomaly score, private dashboard on Cloudflare Workers + D1. | 119 vitest + 197 pytest + 4 ctest, exact pcap replay fixtures | C++17, Python, TypeScript, Cloudflare Workers |
| [phishguard](https://github.com/SolomonSmith-dev/phishguard) | LightGBM URL classifier. Found inverted labels and `https://www.` leakage in the PhiUSIIL dataset, fixed both, and locked the fix with leakage regression tests. | Test AUC 0.9943, 1.54% FPR on Tranco top-5,000; 35 tests | Python, LightGBM, FastAPI |
| [agentic-engineering-os](https://github.com/SolomonSmith-dev/agentic-engineering-os) | `agent-team`: Claude Code workers in sandboxed worktrees, every tool call recorded in SQLite, draft PR only after an independent reviewer approves. | 524 tests, CI on Ubuntu and macOS; 14 of 15 build steps merged | Python, Typer, SQLite, srt sandbox |
| [DocMind](https://github.com/SolomonSmith-dev/DocMind) | Local PDF Q&A with page-level citations, prompt-injection filtering on retrieved chunks, JWT auth and rate limits. | 113 tests, CI + Playwright E2E workflow | Python, FastAPI, ChromaDB, Ollama |

## Open source

- [civicband/clerk-fetchers#85](https://github.com/civicband/clerk-fetchers/pull/85) (merged Jul 2026): generic Swagit meeting-video fetcher; any Swagit city is added with two registry entries and no new code.
- [equinor/semeio#895](https://github.com/equinor/semeio/pull/895) (merged May 2026): fixed a pytest-console-scripts deprecation across the test suite.

[solomonsmith.dev](https://solomonsmith.dev) · [LinkedIn](https://www.linkedin.com/in/solomonsmithdev/) · solomonsmithdev@gmail.com
