import customtkinter as ctk
from database import init_db
from ui.login import LoginApp
import auth


def main():
    # Initialize the database (create tables if they don't exist)
    init_db()
    auth.register_agent("T", "1")
    # Create the main application window
    root = ctk.CTk()
    root.title("Gym Management System")
    root.geometry("500x300+400+100")  # Adjust window size as needed

    container = ctk.CTkFrame(root)
    container.pack(fill="both", expand=True)

    # Start the login screen by instantiating the LoginApp frame
    login_app = LoginApp(container)
    login_app.pack(fill="both", expand=True)
    # Run the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
