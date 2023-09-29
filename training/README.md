# Ai-Email-Writer

### How to train
 - Go to [Google Takeout](https://takeout.google.com/u/1/) and download .mbox file of all "Sent" mail
 - From the root directory of this repo, run `python mbox_to_json.py <.MBOX FILE>`, where `<.MBOX FILE>` is replaced with the path to the mbox file you downloaded
 - Run `python generate_descriptions.py`
 - Run `python jsonl_writer.py`
 - Follow the instructions [here](https://platform.openai.com/docs/guides/fine-tuning/create-a-fine-tuned-model) (starting from the section titled "Create a fine-tuned model")