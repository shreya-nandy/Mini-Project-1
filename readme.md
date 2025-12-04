Snake–Water–Gun Game (Python)
This is a simple Python mini-project based on the classic Snake–Water–Gun game (similar to Rock–Paper–Scissors).
The player competes with the computer, which randomly selects its move.

Game Rules :-
🐍Snake - Drinks Water → Snake wins over Water
🔫Gun   - Shoots Snake → Gun wins over Snake
💧Water - Destroys Gun → Water wins over Gun 

Game Encoding :-
 Snake  -> 's' / 'S' ->  '1'            
 Gun    -> 'g' / 'G'  -> '0'            
 Water  -> 'w' / 'W' -> '-1'           
The program uses this mapping to compare choices and decide the winner.

How to Run the Game :-
1. Install Python (if not installed)
2. Save the source code as:
   'snake_water_gun.py'
3. Open terminal / command prompt in the project folder
4. Run the script: python snake_water_gun.py
5. Enter your choice when prompted:
   * 's' or 'S' → Snake
   * 'g' or 'G' → Gun
   * 'w' or 'W' → Water

Project Structure :-
Snake-Water-Gun-Game
── snake_water_gun.py   # Main Game Script
── README.md            # Documentation

Sample Output :-
Enter your choice between s/S for Snake ,g/G for Gun and w/W for Water): s
You chose Snake AND Computer chose Water
You Won!

Future Enhancements :-
* Score tracking (best of 5 / best of 10)
* Play again option (without restarting)

Author
Shreya Nandy
