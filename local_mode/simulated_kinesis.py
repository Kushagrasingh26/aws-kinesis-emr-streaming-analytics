import json
import time
from pathlib import Path
from event_generator import generate_event

OUT_FILE = Path("outputs/kinesis_stream.jsonl")
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    print(f"Writing stream to: {OUT_FILE}")
    with OUT_FILE.open("a", encoding="utf-8") as f:
        while True:
            event = generate_event()
            f.write(json.dumps(event) + "\n")
            f.flush()
            time.sleep(0.02)  # ~50 events/sec
