import json
import time
from transformers import pipeline


# Load the same task set used by Ollama
with open("tasks.json", "r") as file:
    tasks = json.load(file)


# Load Hugging Face model
model = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct"
)


results = []


# Run each task
for task in tasks:

    print(f"\nRunning Task {task['id']}: {task['task']}")

    start_time = time.time()

    result = model(
        task["prompt"],
        max_new_tokens=200,
        max_length=None
    )

    end_time = time.time()

    response_text = result[0]["generated_text"]

    results.append({
        "id": task["id"],
        "task": task["task"],
        "prompt": task["prompt"],
        "response": response_text,
        "time_seconds": round(end_time - start_time, 2)
    })

    print("Response:")
    print(response_text)

    print(f"Time: {round(end_time - start_time, 2)} seconds")


# Save results
with open("results_huggingface.json", "w") as file:
    json.dump(results, file, indent=4)


print("\nAll tasks completed!")
print("Results saved to results_huggingface.json")