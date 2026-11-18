#!/usr/bin/env python3
"""Convert three Markdown prompt collections into separated, auditable JSON/CSV.

No API calls are made. No model code or Pass@1 measurements are invented.
Usage (PowerShell): py prepare_rmt_final.py
Place the script beside the three original .md files.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "RMT_Final_Prepared"
SOURCES = {
    "person_1": "person_1_clear_ambiguous_prompts.md",
    "person_2": "person_2_45_revised_clear_less_explicit_prompt_pairs_python_3.md",
    "person_3": "tasks_45_clear_ambigious.md",
}
SYSTEM = "Solve the programming problem using Python 3. Read from standard input and write to standard output. Return only executable Python 3 source code, without Markdown or explanations."

HEAD = {
    "person_1": re.compile(r"^## Task (?P<ordinal>\d+): Problem ID (?P<id>\d+) \((?P<tier>[^)]+)\)\s*$", re.M),
    "person_2": re.compile(r"^### (?P<tier>introductory|interview|competition) — ID (?P<id>\d+)\s*$", re.M),
    "person_3": re.compile(r"^## Task (?P<ordinal>\d+) — problem_id (?P<id>\d+)\s*$", re.M),
}

PATTERNS = {
    "person_1": (
        re.compile(r"^### Clear Prompt \(Canonical Baseline\)\s*\n```text\s*\n(?P<prompt>.*?)\n```", re.M | re.S),
        re.compile(r"^### Ambiguous Promt\s*\n```text\s*\n(?P<prompt>.*?)\n```", re.M | re.S),
    ),
    "person_2": (
        re.compile(r"^#### Clear prompt\s*\n````text\s*\n(?P<prompt>.*?)\n````", re.M | re.S),
        re.compile(r"^#### Less-explicit prompt\s*\n````text\s*\n(?P<prompt>.*?)\n````", re.M | re.S),
    ),
    "person_3": (
        re.compile(r"^### Clear\s*\n(?P<prompt>.*?)(?=^### Ambigious\s*$)", re.M | re.S),
        re.compile(r"^### Ambigious\s*\n(?P<prompt>.*?)(?=^---\s*$|\Z)", re.M | re.S),
    ),
}

COLUMNS = ["person", "problem_id", "difficulty_tier", "tier_source", "condition", "original_condition_label", "status", "model", "reasoning_effort", "temperature", "top_p", "generated_code_file", "syntax_ok", "test_cases_total", "test_cases_executed", "test_cases_passed", "first_failed_case", "pass_at_1", "failure_type", "runtime_seconds", "error_details"]


def extract(name, original):
    matches = list(HEAD[name].finditer(original))
    tasks = []
    for index, match in enumerate(matches):
        block = original[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(original)]
        clear_match = PATTERNS[name][0].search(block)
        amb_match = PATTERNS[name][1].search(block)
        if clear_match is None or amb_match is None:
            raise ValueError(f"Missing prompt pair: {name}, task index {index + 1}, id={match['id']}")
        clear, ambiguous = clear_match['prompt'].strip(), amb_match['prompt'].strip()
        if not clear or not ambiguous or clear == ambiguous:
            raise ValueError(f"Missing/identical prompt: {name}, id={match['id']}")
        tier = match.groupdict().get("tier")
        tier_source = "source_heading"
        if tier is None:  # This file supplies the IDs but does not label task difficulty.
            # Mark as provisional until verified against original APPS metadata.
            tier = ["Introductory", "Interview", "Competition"][index // 15]
            tier_source = "provisional_ordinal_inference"
        tier = tier.title()
        markers = ["-----Input-----", "-----Constraints-----", "-----Sample Input-----", "-----Output-----"]
        anchors = [(clear.find(a), ambiguous.find(a), a) for a in markers if a in clear and a in ambiguous]
        # Also support non-English separators (e.g. -----Входные данные-----).
        if not anchors:
            common_separators = set(re.findall(r"^-----[^\n]+-----\s*$", clear, re.M)) & set(re.findall(r"^-----[^\n]+-----\s*$", ambiguous, re.M))
            anchors = [(clear.find(x), ambiguous.find(x), x) for x in common_separators]
        anchor = min(anchors, key=lambda x: x[0]) if anchors else None
        tail_same = bool(anchor and clear[anchor[0]:] == ambiguous[anchor[1]:])
        url_match = re.search(r"https?://(?:www\.)?codeforces\.com/problemset/problem/\S+", block)
        url = url_match.group(0).rstrip('])') if url_match else None
        flags = []
        if "[Image]" in clear or "[Image]" in ambiguous:
            flags.append("image_placeholder_in_prompt")
        if not tail_same:
            flags.append("trailing_input_output_sections_differ_or_missing")
        if name == "person_2":
            flags.append("person_2_candidate_requires_independent_review")
            if match['id'] in {"4042", "36"}:
                flags.append("diagram_reconstructed_in_text")
            if match['id'] in {"4030", "4034"}:
                flags.append("hard_easy_version_overlap")
        if tier_source != "source_heading":
            flags.append("difficulty_tier_needs_source_confirmation")
        if len(re.findall(r"[А-Яа-яЁё]", clear)) > 60:
            flags.append("non_english_source_statement")
        tasks.append({
            "problem_id": str(match['id']),
            "task_ordinal": index + 1,
            "difficulty_tier": tier,
            "tier_source": tier_source,
            "source_problem_url": url,
            "clear_prompt": clear,
            "ambiguous_prompt": ambiguous,
            "original_ambiguous_label": "Less-explicit" if name == "person_2" else "Ambiguous",
            "same_preserved_io_and_examples": tail_same,
            "audit_flags": flags,
            "clear_sha256": hashlib.sha256(clear.encode('utf-8')).hexdigest(),
            "ambiguous_sha256": hashlib.sha256(ambiguous.encode('utf-8')).hexdigest(),
        })
    if len(tasks) != 45:
        raise ValueError(f"Expected 45 pairs in {name}, got {len(tasks)}")
    return tasks


def main():
    OUT.mkdir(exist_ok=True)
    inventory = []
    seen_ids = {}
    summaries = []
    for person, source in SOURCES.items():
        original = (BASE / source).read_text(encoding="utf-8-sig")
        tasks = extract(person, original)
        for t in tasks:
            id_ = t['problem_id']
            if id_ in seen_ids:
                raise ValueError(f"Duplicate ID {id_} across {seen_ids[id_]} and {person}")
            seen_ids[id_] = person
        data = {
            "person": person,
            "source_markdown_file": source,
            "source_sha256": hashlib.sha256(original.encode('utf-8')).hexdigest(),
            "common_system_message": SYSTEM,
            "note": "Prepared prompt data only; no generation or correctness test has run.",
            "task_count": len(tasks),
            "prompt_count": len(tasks) * 2,
            "tasks": tasks,
        }
        (OUT / f"{person}_prompts.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        result_path = OUT / f"{person}_results_TEMPLATE.csv"
        with result_path.open('w', newline='', encoding='utf-8-sig') as file:
            w = csv.DictWriter(file, fieldnames=COLUMNS)
            w.writeheader()
            for task in tasks:
                for condition in ('clear', 'ambiguous'):
                    w.writerow({
                        "person": person,
                        "problem_id": task['problem_id'],
                        "difficulty_tier": task['difficulty_tier'],
                        "tier_source": task['tier_source'],
                        "condition": condition,
                        "original_condition_label": ("Clear" if condition == "clear" else task['original_ambiguous_label']),
                        "status": "NOT_RUN",
                    })
        summaries.append({
            "person": person,
            "tasks": len(tasks),
            "prompts": len(tasks)*2,
            "image_placeholder_task_ids": [t['problem_id'] for t in tasks if "image_placeholder_in_prompt" in t['audit_flags']],
            "preserved_io_sections_count": sum(t['same_preserved_io_and_examples'] for t in tasks),
        })
        for task in tasks:
            inventory.append({
                "person": person,
                "problem_id": task['problem_id'],
                "difficulty_tier": task['difficulty_tier'],
                "tier_source": task['tier_source'],
                "io_and_example_sections_same": task['same_preserved_io_and_examples'],
                "audit_flags": ";".join(task['audit_flags']),
                "source_problem_url": task['source_problem_url'] or "",
            })

    with (OUT / "prompt_audit.csv").open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(inventory[0]))
        w.writeheader()
        w.writerows(inventory)
    (OUT / "summary.json").write_text(json.dumps({"task_count": len(inventory), "generation_count_if_one_per_condition": len(inventory)*2, "people": summaries}, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print('Parsed',len(inventory),'unique tasks and',2*len(inventory),'prompts into', OUT)
    for s in summaries:
        print(f" {s['person']}: {s['tasks']} pairs; {s['prompts']} prompts; image placeholders: {s['image_placeholder_task_ids']}; preserved I/O: {s['preserved_io_sections_count']}/45")


if __name__ == "__main__":
    main()
