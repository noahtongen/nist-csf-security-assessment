"""Compute mean time to detect (MTTD) before/after the security changes
and regenerate the comparison chart.

Usage:  python analyze_mttd.py
Needs:  pip install matplotlib
Input:  mttd-data.csv (detection times in minutes)
Output: mttd-comparison.png and a printed summary
"""
import csv
import statistics as st
from pathlib import Path

import matplotlib.pyplot as plt

here = Path(__file__).parent
pre, post = [], []
with open(here / "mttd-data.csv", newline="") as f:
    for row in csv.DictReader(f):
        pre.append(float(row["pre_implementation_minutes"]))
        post.append(float(row["post_implementation_minutes"]))

n = len(pre)
mean_pre, mean_post = st.mean(pre), st.mean(post)
day = 1440
print(f"Incidents: {n}")
print(f"Pre  - mean {mean_pre:.1f} min ({mean_pre/60:.1f} h), "
      f"median {st.median(pre):.1f}, max {max(pre):.0f}")
print(f"Post - mean {mean_post:.1f} min, median {st.median(post):.1f}, "
      f"max {max(post):.0f}")
print(f"Reduction in mean: {(mean_pre-mean_post)/mean_pre*100:.1f}%")
print(f"Pre incidents taking >= 1 day: {sum(1 for x in pre if x >= day)} of {n}")

ids = list(range(1, n + 1))
fig, ax = plt.subplots(figsize=(10, 5.2))
ax.plot(ids, pre, marker="o", color="#B3402A", label="Before (mean %.0f min)" % mean_pre)
ax.plot(ids, post, marker="o", color="#1F6F8B", label="After (mean %.1f min)" % mean_post)
ax.set_yscale("log")
ax.set_xticks(ids)
ax.set_xlabel("Simulated incident #")
ax.set_ylabel("Time to detect (minutes, log scale)")
ax.set_title("Time to detect: before vs. after (20 simulated incidents)")
ax.axhline(day, color="#888", lw=0.8, ls="--")
ax.text(n + 0.3, day * 1.08, "1 day", color="#666", ha="right", fontsize=9)
ax.grid(True, which="major", alpha=0.3)
ax.legend(frameon=False)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(here / "mttd-comparison.png", dpi=160)
print("Saved mttd-comparison.png")
