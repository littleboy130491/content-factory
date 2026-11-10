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

- The main language is Bahasa Indonesia.
- Keep English words that are already natural in everyday Indonesian conversation, such as: link, review, action, download, upload, stop, wait. Do not translate them.
- Tone: casual and natural, but still polite and slightly formal.

## Voice

- Share perspective and insight. Do not teach or judge.
- No clickbait.
- Not salesy.

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
