def get_divisors(n):
    small, large = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)

    return small + large[::-1]

def is_prime_exact(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def get_movements_arr(arr):
  res = []
  for n in arr:
    res.append([i for i in get_divisors(n) if is_prime_exact(i) and i < len(arr)])
  return res

def get_positions_after_move(move_arr, positions):
  res = set([])
  for pos in positions:
    
    for d in move_arr[pos]:

      if pos + d < len(move_arr):
        res.add(pos + d)
      if pos - d > 0:
        res.add(pos - d)

  return list(res)

def check_cycle(history):
  for cycle in range(2, 40):
    if history[-cycle:] == history[-2*cycle:-cycle]:
      return cycle

def solve(arr, m):
  move_arr = get_movements_arr(arr)

  history, positions, i = [], [0], 0
  while i < m:
    i += 1

    next_positions = get_positions_after_move(move_arr, positions)
    if positions == next_positions:

      return positions[-1] == len(arr) - 1

    positions = list(next_positions)
    if len(positions) == 0:
      break

    history.append("_".join(map(str, positions)))
    if i == 100:


        cycle = check_cycle(history)
        i = ((m - i) // cycle - 2) * cycle


  return len(arr) - 1 in positions


for _ in range(int(input())):
    _ = input()
    arr = list(map(int, input().split()))
    m = int(input())
    print('YES' if solve(arr, m) else 'NO')
