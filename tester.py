import subprocess

fen = "8/8/7p/R2b2P1/3k2P1/2n2K2/8/8 w - - 0 1"

# Start stockfish
engine = subprocess.Popen(
    ["stockfish"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True
)

# Send commands to Stockfish
commands = [
    f"position fen {fen}",
    "go depth 15",  # or use "go movetime 1000" for 1s thinking time
]

for cmd in commands:
    engine.stdin.write(cmd + "\n")
engine.stdin.flush()

# Read output
best_move = None
while True:
    output = engine.stdout.readline().strip()
    if "bestmove" in output:
        best_move = output.split()[1]
        break

engine.stdin.write("quit\n")
engine.stdin.flush()

print("♟️ Best move:", best_move)


