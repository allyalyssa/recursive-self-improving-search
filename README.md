# Recursive Self-Improving Search

SearchHack project exploring whether a search agent can use evidence from previous attempts to improve the way it searches.

- [SearchHack project tree](nodes/5a004683-3bed-443c-98e9-d011b1e0f5c4/node.md)
- [SiftText Knowledge Base](nodes/38a9fc79-8a84-494d-a962-2ec5134bc856/node.md), copied from [SiftText Core](https://github.com/gojack10/sifttext-core/commit/3975312b8f6ede794dd0eefed1c9d2ab77aee19a).

## Reading the knowledge tree

Agents can work directly with the Markdown files in this repo using their usual file tools. SiftText, `rg`, and `fd` are optional.

1. **Start at the root.** Read the [SearchHack project node](nodes/5a004683-3bed-443c-98e9-d011b1e0f5c4/node.md) for project context. For SiftText usage and conventions, start with the [bundled onboarding entry](nodes/5e565245-14fe-406c-977c-cf94a9be246b/node.md).
2. **Walk the tree.** Each node lives at `nodes/<id>/node.md`. Its `children/` directory lists the IDs of its immediate children. Open `nodes/<child-id>/node.md` for each relevant child and repeat as needed. This works even when your checkout or file viewer displays the child links as plain files. Relative Markdown links and `see_also` IDs point to related nodes.
3. **Search if you need a starting point.** Use your file search tool, or run the commands below from the repo root. Search covers both the project tree and the bundled KB. Use the child links to confirm which nodes belong to the project, then read the full matching node for context.

```sh
cat nodes/5a004683-3bed-443c-98e9-d011b1e0f5c4/node.md
ls nodes/5a004683-3bed-443c-98e9-d011b1e0f5c4/children
find nodes -name node.md -type f -exec grep -inF 'recursive search' {} +
```

To update an existing project node, edit its `node.md` and preserve its UUID and placement in the tree. Commit the edit through the team's GitHub workflow.
