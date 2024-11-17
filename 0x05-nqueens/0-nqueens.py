import sys

def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe.
  """
  # Check row on left side
  for i in range(col):
    if board[row][i] == 1:
      return False
  
  # Check upper diagonals
  i = row
  j = col
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1
  
  # Check lower diagonals
  i = row
  j = col
  while i < len(board) and j >= 0:
    if board[i][j] == 1:
      return False
    i += 1
    j -= 1
  
  # No conflicts found
  return True

def solve_n_queens(board, col):
  """
  Solves the N-queens problem recursively.
  """
  # Base case: All queens are placed
  if col >= len(board):
    # Print the solution (board)
    for row in board:
      print([i for i, val in enumerate(row) if val == 1])
    return

  # Try placing queen in all possible rows of current column
  for row in range(len(board)):
    if is_safe(board, row, col):
      board[row][col] = 1
      solve_n_queens(board, col + 1)
      board[row][col] = 0  # Backtrack

def main():
  """
  Main function that handles user input and program execution.
  """
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)
  
  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)
  
  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)
  
  # Create empty chessboard
  board = [[0 for _ in range(n)] for _ in range(n)]
  
  # Solve and print solutions
  solve_n_queens(board, 0)

if __name__ == "__main__":
  main()
