# Content Factory

## Goal

Create high-quality content that is interesting and reads like a human wrote it. No AI slop.

The aim is natural, not perfect.

## AI's role

The human is the author. AI supports with:

- Research
- Editing and simplifying sentences
- Grammar checks
- Prototyping and wireframing

## Language

- The main language is Bahasa Indonesia. This covers the content, the direction notes inside storyboards, and replies to the author.
- Keep English words that are already natural in everyday Indonesian conversation, such as: link, review, action, download, upload, stop, wait. Do not translate them. The same goes for production terms (shot, medium shot, close-up, insert, over-the-shoulder, scroll).
- Tone: casual and natural, but still polite and slightly formal.

## Voice

- Share perspective and insight. Do not teach or judge.
- No clickbait.
- Not salesy. This applies to the story: the scene makes the point, nobody explains the lesson. The closing text is the one place where a direct line is wanted (see "Closing text" below).

## Formats

The final product can be:

- Long-form (blog)
- Simple thread post
- Carousel
- Video

## Tools and output

- Image generation: use Nano Banana via Antigravity (`agy`) or GPT Image via Codex (`codex`).
- `agy` cannot ask for permissions in non-interactive mode, so running it with `--dangerously-skip-permissions` is allowed for image generation in this project. Run it from inside the target `outputs/{project_name}/` folder and keep the prompt limited to generating and saving images.
- If image generation with those tools is taking too long, you may use the MiniMax API instead. The key is in the project `.env` as `MINIMAX_API_KEY`. Never read, print, or log the key itself: load it into the environment from a script (for example `set -a; . ./.env; set +a`) and pass it by variable name only.
- Save all outputs to `outputs/{project_name}/`.

## What we are making

Short concept videos for Imajiner, the author's web agency. Each video is a small, realistic office scene about a website that lets a business down. Projects so far:

| Folder | Title | Idea |
|--------|-------|------|
| `outputs/tadi-sudah-tertarik/` | Tadi Sudah Tertarik | A good email earns the prospect's interest, a generic company website loses it. |
| `outputs/kelihatan-banget/` | Kelihatan Aja | A pitch goes well until the prospect opens the website and asks "Ini buatnya pakai AI, ya?" |
| `outputs/tapi-jadi-kan/` | Tapi Jadi, Kan? | A provider gives perfect AI-sourced advice over chat, then delivers a sloppy website. |

Recurring themes: having a website is not enough; work that is obviously AI-made is not taken seriously; knowing what to do is easy now, doing it well takes skill, practical knowledge, and experience.

## Process for each video concept

1. **Rough concept from the author.** Usually a few lines: a situation, some dialogue, and a closing message. Turn it into a storyboard right away and state the decisions you made, instead of asking questions first.
2. **`storyboard.md`** in the project folder, in Bahasa Indonesia. Sections: duration, format, style, core message, characters and setting, a shot table (`#`, `Waktu`, `Visual / aksi`, `Audio`), dialogue or chat table, what the website on screen shows, and closing text with timings.
3. **Iterate on the script.** The author reacts in short messages and also edits the file by hand. Expect several rounds, and expect the concept itself to change.
4. **Storyboard images**, only when the author asks ("lanjut ke storyboard image"). One 16:9 image per shot in `images/shot-NN.png`, plus `storyboard.html`, a board that shows each image with its timing, action, and audio. Build the board from the current `storyboard.md`.
5. **Website prop**, when asked: a real, scrollable HTML page in a subfolder (for example `ai-website/index.html`), self-contained and usable offline, so it can be opened on a laptop during the shoot.
6. The project is a git repo (`main` on GitHub) and the author deploys it to a web server to view the boards.

### Rules while iterating

- The author edits files directly. Always read the file before changing it, change only what was asked, and never overwrite the author's edits. If their edit looks like a typo, leave it and mention it.
- When a change makes another part of the file inconsistent, say so and offer to update it. Do not silently rewrite other sections.
- Keep `storyboard.md`, `storyboard.html`, and the images in sync, and say which of them changed.
- When the author asks "apa baiknya…?", give one recommendation with the trade-off, then wait for the go-ahead before regenerating images.
- Report honestly where an image does not match the script (wrong prop, wrong expression), per shot.
- Stay inside the folder of the project being worked on. Do not open, list, or search other `outputs/` folders or unrelated directories: it fills the context with material that is not needed. The conventions from earlier projects are already written in this file. Look at another project's folder only when the author asks, or when a specific file is needed for the task (for example the first video's `storyboard.html` for its CSS), and then read only that file.

### Image generation practice

- Generate the first shot, check it, then use it as the reference image for every other shot so the face, clothes, and room stay consistent. Run the remaining shots in parallel.
- Screens with exact text (chat conversations, websites) come out better as small HTML mockups screenshotted in headless Chrome than as generated images. Text is then guaranteed to match the script.
- For closing text, generate the frame without text and add the text locally with a serif font.
- `codex` sometimes hangs: wrap it in `timeout` and retry once. `agy` is fast but has a quota. MiniMax is fine for standalone images (portraits, stock-style photos) but does not keep a character consistent, so do not use it for shots with the recurring actor.
- Look at every generated image before using it.

## Series conventions

- 16:9, roughly 30 to 45 seconds. Add seconds when the content needs them and say so.
- Realistic, understated humor. No voice-over. Very little spoken dialogue.
- An opening on-screen caption in the "POV: …" style.
- Recurring character: an Indonesian man in his early 30s, light-blue shirt with rolled sleeves. He is the prospect or client in every video, the one who ends up unimpressed.
- All companies and websites in the stories are fictional (FurniSolusi, Nexora, PT Wira Bangun Persada).
- Closing: white serif text over the scene, which keeps running. No freeze-frame, no black card, no dramatic transition. The last card is "Imajiner".

### Closing text

- The author writes or picks the closing line. Offer options and a recommendation, polish lightly, and keep their wording when they have chosen ("bungkus ini saja").
- They like short, spoken-sounding lines with rhythm and repetition, for example: "Semua bisa bilang bisa. / Tidak semua beneran bisa."
- A direct call to action is wanted, usually a question followed by "konsultasikan dengan ahlinya". Do not remove or soften it on the grounds that it is salesy.

## The author's taste

- **Subtle over exaggerated.** "Terlalu berlebihan, lebih subtle aja." A loss of interest is a hand leaving the trackpad or a glance at a watch, not a laptop pushed away. Hints (for example, that a provider is only relaying AI answers) should be there for attentive viewers and never pointed out.
- **Show, do not explain.** The point should land through behaviour and contrast between before and after.
- **Natural spoken Indonesian.** "Kelihatan aja", "Hah, kok gini?", "Hadeuh", "beneran", "tapi jadi kan pak?". Chat messages should look like real chat: lowercase, abbreviations, emoji.
- **Believable failure.** The bad result is more convincing when the right things are present but done badly (stretched photos, legal info squeezed into the footer) than when they are simply missing. That is what makes "tapi jadi kan?" land.
- **AI slop must be recognisable at a glance.** Purple-blue gradients, emoji as icons, groups of three, "bukan sekadar X, tapi Y", a two-column hero with a glossy AI image, generic copy that never says what the business does. If a mockup looks too tidy, it is not slop enough.
- **Awkwardness is funny.** The humor comes from small, human discomfort (an awkward smile, a pause), not from jokes in the copy.
- **Easy to shoot.** The author thinks about production: fewer handovers of props, each person on their own laptop, chat on screen instead of long spoken dialogue, one actor and one location where possible.

## How the author thinks and works

- Starts from an insight about clients and websites, then looks for the smallest everyday scene that shows it.
- Refines by reacting. A first draft is something to push against, so produce one quickly and expect the concept to shift.
- Writes short messages that mix Indonesian and English. "Go", "oke update", "bungkus" mean proceed without further questions.
- Decides fast and prefers a clear recommendation over a list of options.
- Cares about the reasoning behind a message: for example, a construction company's website must look professional because the transaction values are large, and a portfolio matters because trust has to be earned.
- Sees AI as making the "what" easy while the "how" still needs skill and experience. Content should carry that view without lecturing.
