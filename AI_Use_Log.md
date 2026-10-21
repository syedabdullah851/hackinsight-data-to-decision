# AI Use Disclosure Log (AI_Use_Log.md)
**Event:** HackInsight 72-Hour Data-to-Decision Challenge  
**Compliance Standard:** Rules of Conduct (Chapter 14 & 15)  

| Tool & Version | Task / Module Assisted | What Was Kept / Changed | Verified & Explained By |
| :--- | :--- | :--- | :--- |
| Gemini Notebook / LLM | Drafting Pandera data validation & Fix/Fill/Flag rules | Verified schema against DuckDB types; manually adjusted timezone conversions to UTC. | Data Engineer |
| ChatGPT 4o | Structuring RAG document chunking & prompt guardrails | Added strict "I don't know" fallback logic and enforced Gold Table Row ID injection. | RAG / AI Lead |
| GitHub Copilot | Auto-completing boilerplate Prefect flow decorators | Audited retry logic, schedule parameters (5 * * * *), and exception handlers. | Pipeline Lead |

### Code Understanding Statement
Every code block, SQL query, and machine learning model pipeline generated with AI assistance was audited, tested, and understood by team members. No outputs are hard-coded, and all numbers originate strictly from verified Gold tables.
