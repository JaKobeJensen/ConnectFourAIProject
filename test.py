from codes import Codes
from connect_four_guis import ConnectFourGui, MainMenuGui


def main_menu():
    main_menu_gui = MainMenuGui(scaling_factor=1.0)
    code = main_menu_gui.start()
    if code is Codes.QUIT:
        quit()
    elif code is Codes.PLAYER_VS_PLAYER:
        print("Player VS Player Button was pressed")
    elif code is Codes.PLAYER_VS_COMPUTER:
        print("Player VS Computer Button was pressed")
    elif code is Codes.COMPUTER_VS_COMPUTER:
        print("Computer VS Computer Button was pressed")
    elif code is Codes.TRAIN_COMPUTER:
        print("Train Computer Button was pressed")
    return


def connect_four():
    connect_four_gui = ConnectFourGui(
        player1_name="Player 1", player2_name="Player 2", scaling_factor=1.0
    )
    connect_four_gui.start()


def main():
    # main_menu()
    connect_four()


if __name__ == "__main__":
    main()
    quit()
