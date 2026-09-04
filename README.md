# From 1 + 1 to an AI Agent

Learn how modern AI systems work by building a continuous chain of small, observable experiments—from the simplest computation to a mini LLM and an AI agent.

## Languages

- [简体中文](docs/zh-CN/README.md)
- [English](docs/en/README.md)
- [日本語](docs/ja/README.md)

## Learning path

```text
Basic mechanisms → Neural networks → Transformer → LLM
→ Inference and runtime → RAG / MCP → Agent → Final AI system
```

Each lab is designed around one question and one verifiable causal chain. The goal is not merely to run code, but to explain why the observed result occurs.

## Labs

- [Browse all labs](labs/README.md)
- [LAB-0001 — How can a computer know that 1 + 1 = 2?](labs/01-foundations/LAB-0001/README.md)

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── en/
│   ├── ja/
│   └── zh-CN/
└── labs/
    ├── README.md                 # Searchable lab catalog
    └── 01-foundations/           # Learning stage
        ├── README.md             # Stage index
        └── LAB-0001/             # Globally unique lab ID
            ├── README.md
            └── experiment.py
```

Future labs follow `labs/<stage>/<LAB-ID>/`. Stage numbers preserve the learning order, while globally unique lab IDs make experiments easy to search and reference.

## Status

This project is being built experiment by experiment. Interfaces, paths, and explanations may evolve as the learning chain becomes clearer.

## License

No license has been selected yet. Until a license is added, all rights are reserved by the repository owner.
