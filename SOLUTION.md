# Low-token lab solution

Open `solution.ipynb` and select the project's `.venv/bin/python` interpreter.
Dependencies are in `requirements-solution.txt`:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-solution.txt
```

Set `OPENAI_API_KEY` in the ignored `.env` file. Run the notebook from top to bottom once. Saved outputs show the actual answers, tool choices and chat token counts. Embedding tokens are not included in the chat counter. Running the question cells again makes new paid chat calls.

The two small datasets are included. The Python Club handbook is original fictional data; the Ruff reference cites its official source. Document and query embeddings are cached in ignored `.lab_cache/`. The notebook uses the lab's LangChain 0.2 APIs and caps retrieval, response length and agent iterations. A multi-hop question uses both tools; a final single-source test demonstrates direct return.

Review the notebook outputs before submitting `solution.ipynb`, both new dataset files and `requirements-solution.txt`. Never commit `.env`, `.venv` or `.lab_cache`.
