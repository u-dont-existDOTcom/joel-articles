# Episode 008 — Railway sentence-engineering comparison arm E2

Date: 2026-09-19
Status: **EXTERNAL FRESH AGENT / PER-SENTENCE ENGINEERING TICKETS / PENDING PANGRAM**

Provider surface:
Railway Agent, new thread, no infrastructure actions.

Method:
The agent was explicitly forbidden to rewrite the paragraph holistically. It received five local editing tickets and returned replacements independently, with no transition optimization.

## Replacement units returned

1. You go over the same event again. You were hurt. What you did afterward may have made things worse.

2. Have I processed this? A little later: Have I really processed it?

3. Halfway through, you notice something you missed before.

4. The thoughts follow the same path again, and dinner is getting cold.

5. You leave the question where it is. Still uncertain, you pick up your fork.

## Integrated exact paragraph for measurement

You go over the same event again. You were hurt. What you did afterward may have made things worse. Have I processed this? A little later: Have I really processed it? Halfway through, you notice something you missed before. The thoughts follow the same path again, and dinner is getting cold. You leave the question where it is. Still uncertain, you pick up your fork.

## Evidence boundary

This arm tests a stronger version of the owner's engineering-attractor hypothesis than E1:
the generator is not asked to produce or integrate a paragraph at all; it executes local sentence tickets, and integration is mechanical.

Any detector improvement must still be checked against preservation because local execution can delete source functions while improving surface shape.