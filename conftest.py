import os
import pytest

# Detect if running in CI
is_ci = os.getenv("CI") is not None

def pytest_configure(config):
    # Ensure report directory exists
    os.makedirs("playwright-report", exist_ok=True)

    # Retries (1 on CI, 0 locally)
    reruns = 1 if is_ci else 0
    config.option.reruns = reruns

    # Workers (1 on CI, auto locally)
    workers = 1 if is_ci else "auto"
    config.option.numprocesses = workers

    # Timeout per test (60s)
    config.option.timeout = 60
