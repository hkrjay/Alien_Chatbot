from secrets import choice
from playsound import playsound

def Music():
    print("===Here are Some Musics===\n")
    print("\n1: Excuses(AP Dhillion)")
    print("2: Brown Munde(AP Dhillion)")
    print("3: Insane(AP Dhillion)")
    print("4: We-Rollin-Shubh")
    print("5: Glass-Animals(English)")
    print("6: Aaja Ve Mahiya(Naresh-Narayan)\n")

    choice=int(input("Choose Your song: "))

    if choice == 1:
        input("\nPress Enter to Play")
        playsound("E:\Doc\pyProject\music\Excuses.wav")

    elif choice == 2:
        input("\nPress Enter to Play")
        playsound("E:\Doc\pyProject\music\Brown-Munde.wav")
    elif choice == 3:
        input("\nPress enter to play")
        playsound("E:\Doc\pyProject\music\Insane.wav",'rb')
    elif choice ==4:
        input("\nPress Enter to play")
        playsound("E:\Doc\pyProject\music\We-Rollin-Shubh.wav")
    elif choice ==5:
        input("\nPress Enter to play")
        playsound("E:\Doc\pyProject\music\Glass-Animals-.mp3")
    elif choice ==6:
        input("\nPress Enter to play")
        playsound("E:\Doc\pyProject\music\Aaja-Ve-Mahiya.mp3")



    else: print("Invalid Choice")
        
Music()