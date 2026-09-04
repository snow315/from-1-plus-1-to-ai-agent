# From `1 + 1 = 2` to an AI Agent

[简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Home](../../README.md)

## Goal

This project builds a continuous understanding of computation, mini LLMs, and AI agents through small experiments that can be run, observed, and explained.

Instead of collecting disconnected facts or only calling existing frameworks, every important mechanism is examined through five questions:

1. How is the input represented?
2. What transformation does the system perform?
3. What can we observe?
4. Why does that result occur?
5. How does this mechanism connect to the next stage?

## Learning path

```text
Basic mechanisms → Neural networks → Transformer → LLM
→ Inference and runtime → RAG / MCP → Agent → Final AI system
```

## Experiment principles

- Each experiment answers one core question.
- Make a prediction before running it.
- Use the smallest readable code that exposes the mechanism.
- Support conclusions with observable evidence.
- Include adjacent concepts only when they are required by the current causal chain.

## Current labs

- [Browse all labs](../../labs/README.md)
- [LAB-0001: How can a computer know that `1+1=2`?](../../labs/01-foundations/LAB-0001/README.md)

## Running a lab

Open the lab's `README.md`, make the requested prediction, and then run its code. For example:

```powershell
python .\labs\01-foundations\LAB-0001\experiment.py
```

Keep your prediction, output, and explanation. A lab is complete when you can explain why the result occurred—not merely when the code runs.
