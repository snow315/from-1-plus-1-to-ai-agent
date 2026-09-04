# Lab Catalog / 实验目录 / 実験一覧

[Home](../README.md) · [简体中文](../docs/zh-CN/README.md) · [English](../docs/en/README.md) · [日本語](../docs/ja/README.md)

This is the single searchable index for every experiment in the project.

这是项目全部实验的统一检索入口。

このページは、プロジェクト内のすべての実験を検索するための統一インデックスです。

## Stages

| Stage | Topic | 中文 | 日本語 | Status |
|---|---|---|---|---|
| `01` | [Foundations](01-foundations/README.md) | 基础机制 | 基本メカニズム | Active |
| `02` | Neural networks | 神经网络 | ニューラルネットワーク | Planned |
| `03` | Transformer | Transformer | Transformer | Planned |
| `04` | LLM | 大语言模型 | 大規模言語モデル | Planned |
| `05` | Inference and runtime | 推理与运行 | 推論とランタイム | Planned |
| `06` | RAG and MCP | RAG 与 MCP | RAG と MCP | Planned |
| `07` | Agents | AI Agent | AI Agent | Planned |
| `08` | Final AI systems | 最终 AI 系统 | 最終 AI システム | Planned |

Planned stages are listed here for navigation but receive a directory only when their first experiment is created. This avoids empty scaffolding.

## All labs

| ID | Stage | Experiment | Necessity | Status |
|---|---|---|---|---|
| `LAB-0001` | `01` Foundations | [How can a computer know that `1+1=2`?](01-foundations/LAB-0001/README.md) | 主链必须 | Ready |

## Naming convention

```text
labs/<two-digit-stage>/<LAB-four-digit-ID>/
```

- Stage numbers express learning order; they do not change when more labs are inserted.
- Lab IDs are globally unique and never reused.
- Every lab owns its code, assets, outputs, and README inside one directory.
- Files shared by multiple labs belong at the nearest common stage directory, not inside an unrelated lab.

Example:

```text
labs/
└── 01-foundations/
    ├── README.md
    ├── LAB-0001/
    │   ├── README.md
    │   └── experiment.py
    └── LAB-0002/
        ├── README.md
        └── experiment.py
```
