#!/usr/bin/env python3
"""Verify the public AXIOM showcase evidence and integrity manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST_SHA256.txt"
SUMMARY = ROOT / "evidence" / "verification-summary.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def verify_summary() -> None:
    data = json.loads(SUMMARY.read_text(encoding="utf-8"))
    if data.get("verification_status") != "PASS":
        raise SystemExit("SHOWCASE_CHECK=FAIL reason=verification_status")
    counts = data.get("counts", {})
    expected = {
        "platform_tests": 406,
        "governance_skills": 5,
        "gpt_to_skills_migrations": 5,
        "emblematic_profiles": 4,
        "emblematic_scenarios": 16,
        "persistence_recovery_scenarios": 10,
        "claim_evidence_entries": 20,
    }
    if counts != expected:
        raise SystemExit("SHOWCASE_CHECK=FAIL reason=unexpected_counts")


def manifest_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path != MANIFEST
        and "__pycache__" not in path.parts
    )


def build_manifest() -> None:
    lines = [
        f"{sha256(path)}  {path.relative_to(ROOT)}"
        for path in manifest_files()
    ]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_manifest() -> int:
    listed: set[str] = set()
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            raise SystemExit(f"SHOWCASE_CHECK=FAIL reason=manifest path={relative}")
        listed.add(relative)

    actual = {str(path.relative_to(ROOT)) for path in manifest_files()}
    if actual != listed:
        raise SystemExit("SHOWCASE_CHECK=FAIL reason=manifest_coverage")
    return len(listed)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-manifest", action="store_true")
    args = parser.parse_args()
    if args.build_manifest:
        build_manifest()
    verify_summary()
    files = verify_manifest()
    print(f"AXIOM_SHOWCASE_CHECK=PASS files={files} platform_tests=406 scenarios=16")


if __name__ == "__main__":
    main()
