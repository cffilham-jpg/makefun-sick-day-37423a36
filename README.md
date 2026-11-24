# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/cffilham-jpg/makefun-sick-day-37423a36/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/cffilham-jpg/makefun-sick-day-37423a36/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

One line, under 200 characters: the funniest excuse for calling in sick to skip work. It leans on a reason a boss might half believe — a voice that has completely gone — and lands the laugh mid-line, on a throat that sounds like a dial-up modem, before a quiet second beat closes it.

> My voice is completely gone — I tried to call in but my throat sounds like a dial-up modem, so this text is doing the talking.

Referral code: `fpna5aje`

## How it works

`main.py` holds the chosen line as the constant `LINE`. Its `validate()` checks the line before anything is written: it must be a string of 1–200 characters, a single line with no leading or trailing whitespace, not only whitespace, and free of Unicode control characters (category Cc). `main()` writes the line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory if needed, with no trailing newline — and exits without writing if validation fails.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
