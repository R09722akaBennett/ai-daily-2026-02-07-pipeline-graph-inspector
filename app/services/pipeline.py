from __future__ import annotations

from collections import defaultdict, deque


def inspect_pipeline(steps: list[dict]) -> dict:
    ids = [s["id"] for s in steps]
    idset = set(ids)
    errors: list[str] = []

    for s in steps:
        for d in s.get("deps", []):
            if d not in idset:
                errors.append(f"missing_dep:{s['id']}->{d}")

    # build graph (dep -> dependents)
    indeg: dict[str, int] = defaultdict(int)
    g: dict[str, list[str]] = defaultdict(list)

    for s in steps:
        indeg[s["id"]] += 0

    for s in steps:
        for d in s.get("deps", []):
            if d in idset:
                g[d].append(s["id"])
                indeg[s["id"]] += 1

    q = deque([n for n in ids if indeg[n] == 0])
    topo: list[str] = []
    while q:
        n = q.popleft()
        topo.append(n)
        for nxt in g[n]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    if len(topo) != len(ids):
        errors.append("cycle_detected")

    # mermaid
    lines = ["graph TD"]
    for s in steps:
        sid = s["id"]
        if not s.get("deps"):
            lines.append(f"  {sid}[{sid}]")
        for d in s.get("deps", []):
            if d in idset:
                lines.append(f"  {d} --> {sid}")

    return {
        "ok": len(errors) == 0,
        "errors": errors,
        "mermaid": "\n".join(lines) + "\n",
        "topo_order": topo,
    }
