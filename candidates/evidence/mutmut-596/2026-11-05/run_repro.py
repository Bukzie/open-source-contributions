#!/usr/bin/env python3
"""Run `mutmut run` for the #596 reproduction in an isolated subprocess.

usage: run_repro.py PYTHON PROJECT_DIR RUNS TIMEOUT_SECONDS
Each run: fresh copy of the project, new process group, core dumps disabled,
CPU-time limit, wall-clock timeout (group killed on expiry). Prints one JSON line per run.
Memory limits (RLIMIT_AS) are not reliably enforced on macOS, so none is set.
"""
import json, os, resource, shutil, signal, subprocess, sys, tempfile, time

py, proj, runs, timeout = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

def limits():
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CPU, (timeout * 2, timeout * 2))
    os.setsid()

for i in range(1, runs + 1):
    with tempfile.TemporaryDirectory(prefix="repro596-") as tmp:
        work = os.path.join(tmp, "p")
        shutil.copytree(proj, work)
        t0 = time.time()
        p = subprocess.Popen([py, "-m", "mutmut", "run"], cwd=work, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, preexec_fn=limits)
        timed_out = False
        try:
            out, _ = p.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(p.pid, signal.SIGKILL)
            out, _ = p.communicate()
        rc = p.returncode
        out = out.replace(tmp, "<tmp>").replace(os.path.expanduser("~"), "~")
        print(json.dumps({"run": i, "returncode": rc, "signal": -rc if rc < 0 else None,
                          "timed_out": timed_out, "seconds": round(time.time() - t0, 1),
                          "output_tail": out[-700:]}), flush=True)
