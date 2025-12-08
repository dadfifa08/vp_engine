# -*- coding: utf-8 -*-
"""
Main entrypoint for the TiraPalos Engine.
Runs all background workers in a continuous, fault-tolerant loop.
Designed for scalable cloud deployment (Railway).
"""

import time
import traceback
from utils.logger import log
from social.threader import run_threads


def safe_execute(task_fn, task_name: str):
    try:
        log(f"▶️ Starting task: {task_name}")
        task_fn()
        log(f"✅ Completed task: {task_name}")

    except Exception as e:
        log(f"❌ Error in task '{task_name}': {e}")
        log(traceback.format_exc())


def main_loop():
    log("🚀 TiraPalos Engine Started (Cloud Mode)")
    time.sleep(3)

    failure_count = 0

    while True:
        try:
            safe_execute(run_threads, "Twitter Thread Engine")
            failure_count = 0

        except Exception as loop_error:
            log(f"🔥 Engine-level error: {loop_error}")
            log(traceback.format_exc())
            failure_count += 1
            backoff = min(60, 5 * failure_count)
            log(f"⏳ Backing off for {backoff} seconds...")
            time.sleep(backoff)
            continue

        log("⏳ Sleeping 30 seconds before next cycle...")
        time.sleep(30)


if __name__ == "__main__":
    main_loop()
