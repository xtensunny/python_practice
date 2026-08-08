# Chapter 8 Concatenating text strings

print(" --- Chapter 8 Concatenation --- ")

# 1. Concatenating strings - my chess profile stats
print("\n --- My Chess Profile Stats --- ")

game = "Chess"
strength_rapid = "1200 elo"
strength_blitz = "1180 elo"
strength_bullet = "900 elo"
preference = "I prefer playing blitz, "
reason = "because it's balanced... nor too fast neither too slow."

print(f"\nGame: {game}")
print(f"Rapid: {strength_rapid}")
print(f"Blitz: {strength_blitz}")
print(f"Bullet: {strength_bullet}")
print(f"Prefered Time Control: {preference} {reason}")   # concatenated sentence


# 2. Concatenating variables - Favorite chess players 
print("\n --- Favorite Chess Players ---")

no_1 = "Bobby Fischer"
no_2 = "Mikhail Tal"
no_3 = "Hikaru Nakamura"
their_fide_rating = "---" + no_1 + ": 2785--- " + no_2 + ": 2705--- " + no_3 + ": 2816--- "

print(f"\n1st: {no_1}")
print(f"2nd: {no_2}")
print(f"3rd: {no_3}")
print(f"Their Peak Fide Rating: {their_fide_rating}")