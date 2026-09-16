# Assignment 5 — Local Ollama vs Hugging Face Workflow

## 1. Objective

The objective of this assignment is to compare two AI workflows on the same set of text-generation tasks:

1. Ollama running locally on the computer
2. Hugging Face running in Google Colab

The same five prompts were used for both workflows to make the comparison fair.

---

## 2. Task Set

The following five tasks were tested:

1. Summarization
2. Sentiment Classification
3. Information Extraction
4. Question Answering
5. Reddit Comment Generation

---

## 3. Workflow A — Ollama

### Setup

- Platform: Local Windows computer
- Tool: Ollama
- Model: `llama3.2:3b`
- Model size: 2.0 GB
- Inference: Local

Ollama was installed locally and the `llama3.2:3b` model was downloaded using the Ollama CLI.

### Results

| Task | Time | Result |
|---|---:|---|
| Summarization | 15.16 sec | Successful |
| Sentiment Classification | 11.48 sec | Successful |
| Information Extraction | 10.12 sec | Failed |
| Question Answering | 8.98 sec | Successful |
| Reddit Comment Generation | 58.10 sec | Successful |

**Total execution time: 103.84 seconds**

### Observations

- Ollama completed the tasks relatively quickly on the local computer.
- The model successfully handled summarization, sentiment classification, question answering, and Reddit comment generation.
- The information extraction task failed because the model incorrectly stated that the input text was not provided.
- The Reddit comment generation task took the longest time among the Ollama tasks.

---

## 4. Workflow B — Hugging Face

### Setup

- Platform: Google Colab
- Library: Hugging Face Transformers
- Model: `Qwen/Qwen2.5-1.5B-Instruct`
- Inference: Google Colab

The Hugging Face model was loaded using the Transformers library and tested using the same five prompts used for the Ollama workflow.

### Results

| Task | Time | Result |
|---|---:|---|
| Summarization | 164.77 sec | Successful |
| Sentiment Classification | 45.98 sec | Successful |
| Information Extraction | 97.24 sec | Successful |
| Question Answering | 115.44 sec | Successful |
| Reddit Comment Generation | 118.08 sec | Partially generated |

**Total execution time: 541.51 seconds**

### Observations

- The Hugging Face workflow successfully handled the information extraction task that Ollama failed.
- The model generally produced detailed responses, sometimes providing more information than requested.
- The question-answering response included additional information beyond the answer required by the prompt.
- The Reddit comment generation response was truncated before completing the full output.
- The workflow was considerably slower than the Ollama workflow in this test.
- A Transformers warning was displayed because the model had a default `max_length` setting while `max_new_tokens` was also specified. This was a warning and did not prevent the tasks from running successfully.

---

## 5. Overall Comparison

| Factor | Ollama | Hugging Face / Colab |
|---|---|---|
| Execution | Local computer | Google Colab |
| Model | llama3.2:3b | Qwen2.5-1.5B-Instruct |
| Internet for inference | Not required | Generally required |
| Privacy | Better for local data | Data processed in Colab environment |
| Setup | Simple | Simple |
| Total time in this test | **103.84 sec** | **541.51 sec** |
| Information Extraction | Failed | Successful |
| Output style | Generally concise | More detailed/verbose |
| Model flexibility | Good | Very high |
| Local resource usage | Uses local computer resources | Uses Colab resources |

---

## 6. Performance Comparison

The total execution time was:

- Ollama: **103.84 seconds**
- Hugging Face: **541.51 seconds**

In this test, the Ollama workflow was faster than the Hugging Face workflow.

However, this does not mean that Ollama is always faster than Hugging Face because different models and execution environments were used.

The comparison demonstrates the performance of the two selected workflows under the tested conditions.

---

## 7. Quality Comparison

### Ollama

Ollama produced usable results for 4 out of 5 tasks.

The main failure was the information extraction task, where the model did not correctly use the information already provided in the prompt.

### Hugging Face

Hugging Face successfully handled the information extraction task and produced the required name, email, and age.

However, some responses were more verbose than required, and the Reddit comment generation response was truncated.

---

## 8. Advantages of Ollama

- Runs AI models locally.
- Better suited for keeping sensitive data on the local machine.
- Does not require an internet connection after the model is downloaded.
- Simple command-line interface.
- Faster in our particular test.

---

## 9. Advantages of Hugging Face

- Provides access to a large number of AI models.
- Easy to experiment with different models.
- Can use Google Colab resources instead of relying completely on the local computer.
- Provides a large ecosystem of tools and libraries.
- Useful for research and model experimentation.

---

## 10. Limitations

This experiment used different models:

- Ollama: `llama3.2:3b`
- Hugging Face: `Qwen/Qwen2.5-1.5B-Instruct`

Therefore, the results should be considered a comparison of the two workflows under the tested setup, rather than a direct benchmark proving that one model or platform is universally better.

The Hugging Face workflow was also run in Google Colab, while Ollama was run locally. Hardware and available resources can affect response time.

---

## 11. Conclusion

Both Ollama and Hugging Face are useful approaches for working with AI models.

Ollama is useful when local execution, privacy, and simple deployment are important. In this experiment, it also provided faster inference on the tested task set.

Hugging Face is useful when experimenting with different models and using cloud-based resources such as Google Colab. In this experiment, it successfully handled the information extraction task that Ollama failed, although its responses took longer to generate.

Overall, the experiment demonstrates that the choice between local Ollama and Hugging Face depends on the project requirements, including privacy, available hardware, model flexibility, response quality, and execution speed.