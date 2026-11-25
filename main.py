#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

Writes one ~100-word monologue to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: /output/entry.txt) and prints it.

The speaker is Lord Veylan, three centuries into a reign he won
and now has to administer: skulls in the hallway, a cursed chair,
a ledger that never balances, a hero at the gate every dawn. His
weariness never gets named outright — it leaks through the voice:
trailing sentences, small deflections, a plan recited like a
grocery list, and a final word that quietly forgets what it was
for. He is still a villain: the eclipse, the old gods, the rivers
running black are all still on the schedule. Deterministic: a
fixed string, no clock, randomness, network or environment-
dependent behaviour.
"""

import os

MONOLOGUE = (
    "Come in. Mind the skulls \u2014 I meant to move those. Three "
    "centuries of them, and the help just... stopped answering. Sit. "
    "Not that chair \u2014 cursed. Short version: I wanted the kingdom. "
    "I got it. The crown fits. The ledgers don't. Every dawn, another "
    "hero at the gate, another speech about dawn, and I nod along "
    "because interrupting takes longer than listening. The plan? Oh, "
    "the plan is magnificent. Eclipse at midnight, the old gods awake, "
    "the rivers running black. It only needs one more thing. One "
    "more... what was it? The seal. The seal, then sleep. After the "
    "eclipse. Probably."
)


def main() -> None:
    words = MONOLOGUE.split()
    if not 95 <= len(words) <= 105:
        raise SystemExit(f"word count out of range: {len(words)}")
    if not MONOLOGUE.strip():
        raise SystemExit("monologue is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(MONOLOGUE + "\n")
    except OSError:
        pass
    print(MONOLOGUE)


if __name__ == "__main__":
    main()
