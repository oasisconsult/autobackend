import subprocess
import requests
import time


def validate_runtime(path: str):
    """
    Ensures generated backend actually runs.
    """

    try:
        build = subprocess.run(
            ["docker", "build", "-t", "gen-app", path],
            capture_output=True,
            text=True
        )

        if build.returncode != 0:
            return False, "Docker build failed"

        container = subprocess.Popen(
            ["docker", "run", "-p", "8001:8000", "gen-app"]
        )

        time.sleep(5)

        try:
            res = requests.get("http://localhost:8001/health", timeout=3)

            if res.status_code == 200:
                return True, "OK"

            return False, "Health check failed"

        except Exception as e:
            return False, f"Runtime error: {str(e)}"

    finally:
        subprocess.run(["docker", "stop", "gen-app"], capture_output=True)