#!/usr/bin/env python3
# EXP070 - Autonomous Laboratory

from pathlib import Path
from datetime import datetime, timezone
import subprocess
import csv


BASE = Path(__file__).resolve().parent.parent

RESULT = BASE / "experiments/EXP070_autonomous_lab/results"

PIPELINE = [
    ("VALIDATION", "PYTHONPATH=src python tests/run_scientific.py"),
]


def run_command(cmd):

    print("="*72)
    print(cmd)
    print("="*72)

    result = subprocess.run(
        cmd,
        shell=True,
        cwd=BASE,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)

        raise RuntimeError(
            f"FAILED: {cmd}"
        )


def main():

    RESULT.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now(
        timezone.utc
    ).isoformat()


    status=[]


    print("="*72)
    print("EXP070 AUTONOMOUS LABORATORY")
    print("="*72)


    for name,cmd in PIPELINE:

        try:

            run_command(cmd)

            status.append(
                [name,"OK"]
            )

        except Exception:

            status.append(
                [name,"FAILED"]
            )


    outfile = RESULT / "autonomous_run_report.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(
            [
                "timestamp",
                "phase",
                "status"
            ]
        )


        for phase,result in status:

            writer.writerow(
                [
                    timestamp,
                    phase,
                    result
                ]
            )


    print("="*72)
    print("EXP070 COMPLETE")
    print(outfile)
    print("="*72)



if __name__=="__main__":
    main()

