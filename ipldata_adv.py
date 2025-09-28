import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# -----------------------------
# 1. Create Sample Fielding Data
# -----------------------------
np.random.seed(42)

players = ["Phil Salt", "Yash Dhull", "Axar Patel"]
positions = ["Slip", "Point", "Covers", "Mid-off", "Mid-on", "Fine Leg", "Deep Cover", "Square Leg", "Third Man"]
pick_types = ["clean pick", "good throw", "fumble", "bad throw", "catch", "drop catch", "none"]
throw_types = ["run out", "missed stumping", "missed run out", "stumping", "none"]

rows = []
for over in range(1, 21):       # 20 overs
    for ball in range(1, 7):    # 6 balls per over
        if np.random.rand() < 0.3:  # ~30% balls have a fielding event
            player = np.random.choice(players)
            pos = np.random.choice(positions)
            pick = np.random.choice(pick_types, p=[0.25,0.2,0.1,0.05,0.25,0.1,0.05])
            throw = np.random.choice(throw_types, p=[0.15,0.05,0.02,0.03,0.75])
            if pick in ["catch","drop catch"]:
                throw = "none"

            # Runs impact (positive = saved, negative = conceded)
            if pick == "clean pick":
                runs = np.random.choice([0,1,2])
            elif pick == "good throw":
                runs = np.random.choice([0,1,2,3])
            elif pick == "fumble":
                runs = np.random.choice([-2,-1,0,1])
            elif pick == "bad throw":
                runs = np.random.choice([-3,-2,-1,0])
            elif pick == "catch":
                runs = 0
            elif pick == "drop catch":
                runs = np.random.choice([-4,-3,-2,-1,0])
            else:
                runs = 0
        else:
            player, pos, pick, throw, runs = "", "", "none", "none", 0

        rows.append({
            "Over": over,
            "Ball": ball,
            "Player": player,
            "Position": pos,
            "Pick": pick,
            "Throw": throw,
            "Runs": runs
        })

df = pd.DataFrame(rows)

# -----------------------------
# 2. Calculate Performance Score
# -----------------------------
weights = {"WCP":4, "WGT":3, "WC":6, "WDC":-5, "WST":5, "WRO":8, "WMRO":-6, "WDH":7}

summary = []
for p in players:
    sub = df[df["Player"] == p]
    CP = (sub["Pick"] == "clean pick").sum()
    GT = (sub["Pick"] == "good throw").sum()
    C  = (sub["Pick"] == "catch").sum()
    DC = (sub["Pick"] == "drop catch").sum()
    ST = (sub["Throw"] == "stumping").sum()
    RO = (sub["Throw"] == "run out").sum()
    MRO= (sub["Throw"] == "missed run out").sum()
    DH = np.random.randint(0,3)   # random direct hits
    RS = sub["Runs"].sum()

    PS = (CP*weights["WCP"] + GT*weights["WGT"] + C*weights["WC"] +
          DC*weights["WDC"] + ST*weights["WST"] + RO*weights["WRO"] +
          MRO*weights["WMRO"] + DH*weights["WDH"] + RS)

    summary.append({"Player":p,"CP":CP,"GT":GT,"C":C,"DC":DC,"ST":ST,"RO":RO,
                    "MRO":MRO,"DH":DH,"RS":RS,"PS":PS})

agg = pd.DataFrame(summary)
print("\n--- Fielding Summary ---")
print(agg)

# -----------------------------
# 3. Visualizations
# -----------------------------

# Bar chart of PS
plt.figure(figsize=(7,5))
plt.bar(agg["Player"], agg["PS"], color="skyblue", edgecolor="black")
plt.title("Performance Score by Player")
plt.xlabel("Player")
plt.ylabel("Performance Score")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Radar chart of metrics
metrics = ["CP","GT","C","DC","ST","RO","MRO","DH","RS"]
angles = [n/float(len(metrics))*2*pi for n in range(len(metrics))]
angles += angles[:1]

plt.figure(figsize=(7,7))
for i,row in agg.iterrows():
    values = [row[m] for m in metrics]
    values += values[:1]
    plt.polar(angles, values, label=row["Player"])
    plt.fill(angles, values, alpha=0.1)
plt.xticks(angles[:-1], metrics)
plt.title("Fielding Metrics Comparison")
plt.legend(loc="upper right", bbox_to_anchor=(1.2,1.1))
plt.show()

# Timeline of cumulative runs saved/conceded
plt.figure(figsize=(9,6))
for p in players:
    sub = df[df["Player"] == p].groupby("Over")["Runs"].sum().cumsum()
    plt.plot(sub.index, sub.values, marker="o", label=p)
plt.title("Cumulative Runs Saved/Conceded by Over")
plt.xlabel("Over")
plt.ylabel("Runs (+ saved / - conceded)")
plt.legend()
plt.grid(alpha=0.6)
plt.show()
