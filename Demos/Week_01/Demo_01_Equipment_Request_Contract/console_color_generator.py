"""
Explanation - For printing text in a specific color using ANSI escape codes:

\033[ starts the ANSI escape sequence.
91m, 92m, ... etc., are color codes for different foreground colors.
\033[00m resets the text style so the terminal returns to normal formatting after each print.

"""

for style in [0, 1]:  # 0: normal, 1: bold/bright
    for fg in range(30, 38):
        for bg in range(40, 48):
            code = f"{style};{fg};{bg}"
            print(f"\033[{code}m {code} \033[0m", end=" ")
        print()  # Newline after each row
    print()  # Extra newline between normal and bold
