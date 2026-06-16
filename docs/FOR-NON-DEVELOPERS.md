# Using these rules if you are not a programmer

You do **not** need to know how to code to get a lot out of this. These rules are a set
of instructions that make Cursor's AI behave more like a careful, senior engineer and
less like an over-confident intern. This page explains, in plain language, what they do
for you and how to use them.

If a word here is unfamiliar, check the [tiny glossary](#a-tiny-glossary) at the bottom.

---

## What these rules actually do for you

Without any rules, an AI coding assistant tends to guess, write a lot of code quickly,
and tell you it is "done" whether or not it really works. That is where non-technical
users get burned.

With these rules loaded, the assistant is pushed to:

- **Look before it leaps.** It reads your actual project first instead of assuming.
- **Do the smallest fix that solves your problem**, not a giant rewrite.
- **Prove its work.** For a bug, it reproduces the problem, fixes it, then re-checks that
  it is actually gone. For a visual change, it looks at the result.
- **Tell the truth.** If it is not sure, or it could not test something, it says so
  instead of pretending. It will not invent facts to sound confident.
- **Ask only when it genuinely must.** It will not interrogate you with technical
  questions it could answer by looking at your project itself.
- **Leave your secrets alone.** It is told not to open or print password and key files.

In short: it is engineered to be honest and to verify, which is exactly what you can't
easily check yourself.

---

## Install it in three steps

You need the **Cursor** app (a free download from [cursor.com](https://cursor.com)) and
the folder of rules from this project.

1. **Download this project.** On the project's GitHub page, click the green **Code**
   button, then **Download ZIP**, and unzip it. (Or, if someone set up the project for
   you, it may already be there.)
2. **Copy the `.cursor` folder into your project.** Find the folder named `.cursor`
   inside what you downloaded, and copy it into the top of your own project folder. The
   leading dot is intentional; it may be hidden by default
   (`Cmd+Shift+.` on Mac shows hidden files).
3. **Open your project in Cursor.** That is it. The two core rules turn on automatically.
   Everything else loads by itself only when a task needs it.

You will not see a confirmation popup — the rules work quietly in the background. To
sanity-check, just ask the assistant something and watch it inspect your files before
acting.

---

## How to talk to it

The most important habit: **describe the outcome you want in plain words. Don't try to
describe the technical solution.** You are the person who knows what "good" looks like;
let it figure out the how.

Good, natural requests (these are real, and the assistant handled them well):

| What you type | What it does |
|---|---|
| "my website is really slow please make it fast" | Opens your project, finds the slow part, fixes it, and explains the speedup. |
| "the totals on my sales page don't match my spreadsheet, fix it" | Finds the calculation, reproduces the wrong number, fixes the bug, confirms the total now matches. |
| "make my site work on iphone" | Makes the layout fit a phone screen and the menu tappable, then checks it. |
| "I want people to be able to book appointments with me" | Suggests the simplest option first (often a no-code tool), and asks a couple of quick questions before building anything. |

Notice the pattern: you say the *goal*, not "change the CSS flexbox" or "refactor the
controller." If you knew those words you probably would not need this page.

You can also **paste a screenshot** of something that looks wrong. The assistant can read
images, so a picture of the broken page is often the fastest way to explain a problem.

---

## What to expect back

A good answer will usually tell you, near the end:

- **what it changed** (which files, in plain terms),
- **what it checked** to be sure it worked, and
- **anything it could not verify**, so you know what to test yourself.

You may see status words like these. Here is what they mean for you:

| It says | It means |
|---|---|
| **verified** | It actually tested this and saw it work. |
| **unverified** / **implemented but unverified** | It made the change but could not fully test it — please try it yourself. |
| **blocked** | It hit something it cannot get past and needs your input or access. |
| **assumption** | It made a reasonable guess; double-check if it matters. |

If you ever just see "Done!" with no mention of what was checked, ask: *"How did you
verify this works?"* The rules tell it to answer that honestly.

---

## A few tips that make a big difference

- **Be specific about the goal, vague about the method.** "Make the signup form ask for a
  phone number too" beats "edit the form component."
- **One thing at a time.** Smaller requests get more reliable results than a single giant
  one.
- **If it asks you a question, answer briefly.** It only asks when a choice really matters
  (for example, "do you want customers to pay now or later?").
- **When something is wrong, describe what you see**, not what you think the cause is:
  "the price shows 12 but it should be 12.50" is perfect.
- **Let it test.** If it wants to run your project to check its work, that is the rules
  doing their job. Saying yes is usually the right move.
- **It will not touch your passwords or keys.** The rules forbid reading or printing
  secret files, so you do not have to worry about it leaking them into a chat.

---

## When to bring in a developer

These rules make the assistant safer and more honest, but they are not magic. Loop in a
real developer when:

- the change involves **money, accounts, or private data** and must be exactly right,
- you are about to **publish/deploy** something to real customers for the first time, or
- the assistant says it is **blocked** on something it cannot access (servers, accounts,
  permissions).

A healthy way to think about it: the assistant is a capable junior engineer who now
*shows its work*. That is a big upgrade — but for high-stakes changes, you still want a
senior set of eyes.

---

## A tiny glossary

- **Cursor** — the app you type your requests into; it is a code editor with an AI built in.
- **Project / repo** — the folder that holds your website or app's files.
- **`.cursor` folder** — the folder of rules you copied in; it is what makes the assistant behave well.
- **Terminal** — a text window for typing computer commands. You generally do **not** need it for this; the assistant runs commands for you.
- **Deploy / push** — publishing your changes so other people can see them. Worth a developer's review the first time.

---

Want the short version for developers, or to see how all this was tested against the
model? See the main [README](../README.md) and the [harness](../harness/README.md).
