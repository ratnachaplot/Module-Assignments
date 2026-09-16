import json
import requests
import time

# Load our common task set
with open("tasks.json", "r") as file:
    tasks = json.load(file)

results = []

# Run each task through Ollama
for task in tasks:
    print(f"\nRunning Task {task['id']}: {task['task']}")

    start_time = time.time()

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": task["prompt"],
            "stream": False
        }
    )

    end_time = time.time()

    result = response.json()

    results.append({
        "id": task["id"],
        "task": task["task"],
        "prompt": task["prompt"],
        "response": result["response"],
        "time_seconds": round(end_time - start_time, 2)
    })

    print("Response:")
    print(result["response"])
    print(f"Time: {round(end_time - start_time, 2)} seconds")


# Save results
with open("results_ollama.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nAll tasks completed!")
print("Results saved to results_ollama.json")