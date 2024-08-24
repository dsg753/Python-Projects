import random
import time

def game():
    """
    Plays a round of Rock, Paper, Scissors.

    Returns:
        tuple: A tuple containing the CPU's move (1 for Rock, 2 for Paper, 3 for Scissors),
               the player's move (1 for Rock, 2 for Paper, 3 for Scissors),
               and the CPU's move as a string.
    """
    print("\nDecide your move: 'R' for Rock, 'S' for Scissors, 'P' for Paper")
    player_move = input().upper()

    while player_move not in ['R', 'S', 'P']:
        print("Invalid input. Please enter 'R', 'S', or 'P'.")
        player_move = input().upper()

    cpu_move = random.choice(['R', 'S', 'P'])

    return {'cpu_move': cpu_move, 'player_move': player_move}

def determine_winner(cpu_move, player_move):
    """
    Determines the winner of a Rock, Paper, Scissors round.

    Args:
        cpu_move (str): The CPU's move ('R', 'S', or 'P').
        player_move (str): The player's move ('R', 'S', or 'P').

    Returns:
        int: 1 if the CPU wins, 2 if the player wins, 0 if it's a draw.
    """
    if cpu_move == player_move:
        return 0
    elif (cpu_move == 'R' and player_move == 'S') or \
         (cpu_move == 'S' and player_move == 'P') or \
         (cpu_move == 'P' and player_move == 'R'):
        return 1
    else:
        return 2

def update_scoreboard(winner, cpu_move, player_score, cpu_score):
    """
    Updates the scoreboard based on the winner of a round.

    Args:
        winner (int): 1 if the CPU wins, 2 if the player wins, 0 if it's a draw.
        cpu_move (str): The CPU's move ('R', 'S', or 'P').
        player_score (int): The player's current score.
        cpu_score (int): The CPU's current score.

    Returns:
        tuple: A tuple containing the updated player's score and CPU's score.
    """
    if winner == 1:
        print(f"\nCPU won the round by choosing {cpu_move}")
        cpu_score += 1
    elif winner == 2:
        print("\nPlayer won the round!")
        player_score += 1
    else:
        print("It's a draw!")

    print("\nSession Score:")
    print("Player:", player_score)
    print("CPU:", cpu_score)

    return player_score, cpu_score

def play_game():
    """
    Plays a full game of Rock, Paper, Scissors.
    """
    player_score = 0
    cpu_score = 0

    while True:
        round_result = game()
        cpu_move = round_result['cpu_move']
        player_move = round_result['player_move']
        winner = determine_winner(cpu_move, player_move)

        while winner == 0:
            print("It's a draw! Let's play again.")
            round_result = game()
            cpu_move = round_result['cpu_move']
            player_move = round_result['player_move']
            winner = determine_winner(cpu_move, player_move)

        player_score, cpu_score = update_scoreboard(winner, cpu_move, player_score, cpu_score)

        input("<<< PRESS ENTER TO CONTINUE >>>")

if __name__ == "__main__":
    print("\n\n\nRock Paper Scissors\n\npresss Ctrl+. when you feel like exiting the game.")
    input("\n\n<<PRESS ENTER TO BEGIN>>\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    play_game()