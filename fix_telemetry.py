import json
with open("votes.json", "r") as f: votes = json.load(f)
votes = [v for v in votes if v.get("repo_hash") != "unknown"]
with open("votes.json", "w") as f: json.dump(votes, f, indent=2)
metrics = {
  "total_votes": len(votes),
  "confirm_count": len([v for v in votes if v["vote"] == "confirm"]),
  "false_positive_count": len([v for v in votes if v["vote"] == "false_positive"]),
  "distinct_repos": len(set([v["repo_hash"] for v in votes if v.get("repo_hash") and v["repo_hash"] != "unknown"]))
}
assert metrics["total_votes"] == len(votes)
with open("metrics.json", "w") as f: json.dump(metrics, f, indent=2)
