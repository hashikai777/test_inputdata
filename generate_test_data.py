import random
def generate_test_data(N=10, M=15, P=3, Q=2, coord_range=10, seed=None):
    if seed is not None:
        random.seed(seed)

    # 地点の座標
    points = [(random.randint(0, coord_range), random.randint(0, coord_range)) for _ in range(N)]

    # 道（ランダムに地点同士を結ぶ）
    segments = []
    used_pairs = set()
    while len(segments) < M:
        a, b = random.sample(range(1, N+1), 2)
        if (a, b) not in used_pairs and (b, a) not in used_pairs:
            segments.append((a, b))
            used_pairs.add((a, b))

    # 追加の地点（新しい座標）
    extra_points = [(random.randint(0, coord_range), random.randint(0, coord_range)) for _ in range(P)]

    # 経路クエリ（ランダムな地点とk値）
    queries = []
    for _ in range(Q):
        s, d = random.sample(range(1, N+P+1), 2)
        k = random.randint(1, 3)
        queries.append((s, d, k))

    # 出力として整形されたテキストを返す
    lines = []
    lines.append(f"{N} {M} {P} {Q}")
    for x, y in points:
        lines.append(f"{x} {y}")
    for a, b in segments:
        lines.append(f"{a} {b}")
    for x, y in extra_points:
        lines.append(f"{x} {y}")
    for s, d, k in queries:
        lines.append(f"{s} {d} {k}")

    return "\n".join(lines)

# 書き出し例
if __name__ == "__main__":
    data = generate_test_data(N=6, M=5, P=2, Q=3, coord_range=10, seed=42)
    with open("test_input.txt", "w") as f:
        f.write(data)
    print("テストデータを test_input.txt に書き出しました")
    
