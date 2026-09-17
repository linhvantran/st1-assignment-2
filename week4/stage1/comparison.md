# Comparison — Human vs AI Versions

## Part E — Comparison Table

| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes — small, single-purpose function | Yes — even simpler, just builds and returns a dictionary |
| Runs successfully? | Yes | Yes |
| Uses only required features? | Yes — list, dictionary, function, no database/GUI | Yes — matches the restriction in the prompt exactly |
| Adds assumptions? | No — only assumption is that an empty name is invalid | Assumed no error handling was needed since the prompt didn't explicitly ask for it |
| Handles errors? | Yes — raises `ValueError` for an empty patient name | No — accepts any input, including blank or `None`, without complaint |
| Could I explain it? | Yes, fully | Yes, fully — it's simpler than my version, so easier if anything |

## Part F — Verify Behaviour (test results)

| Test case | Human version | AI version |
|---|---|---|
| Normal appointment | Books and displays correctly | Creates and returns the dictionary correctly |
| Blank patient name (`''`) | Raises `ValueError` as designed | Accepted silently — no validation |
| Two appointments, same practitioner/time | Both get added — no conflict check exists | Same — no conflict check either |
| `patient_name=None` | Raises `ValueError` (`not None` is `True`) | Accepted silently |
| `appointment_time=None` | Accepted without error — not covered by the current check | Accepted silently |

## Five limitations (from running both programs)

1. No check preventing two appointments for the same practitioner at the same time (double-booking).
2. No persistence - all data disappears when the program ends; nothing is saved between runs.
3. No validation on `appointment_time` - a nonsense string would be accepted as a valid time.
4. No way to update or cancel an appointment once it's booked.
5. No search/lookup function - no way to find one patient's appointment without printing everything.