from backend.vector_store import VectorStore

store = VectorStore("data/debug_cases.json")

def analyze_error(error, code):
    query = error + " " + code
    results = store.search(query)

    solutions = []
    scores = []

    for score, item in results:
        solutions.append({
            "fix": item["fix"],
            "cause": item["cause"],
            "confidence": round(score, 2)
        })
        scores.append(score)

    avg_conf = sum(scores) / len(scores) if scores else 0

    return {
        "solutions": solutions,
        "overall_confidence": round(avg_conf, 2),
        "similar_cases_found": len(results),
        "explanation": "Results are based on semantically similar past debugging cases using vector search."
    }