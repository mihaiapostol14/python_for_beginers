# BankAccount Mini Program

This mini program is a simple command-line banking simulation written in Python. It allows users to create bank accounts, deposit and withdraw money, and check their balance, all managed via a PIN system.

## Features

- **Account Creation:** Users can create a new bank account by providing their name and an initial deposit. Each account is assigned a unique 4-digit PIN.
- **Account Access:** Access existing accounts using the assigned PIN.
- **Deposits:** Add funds to your account.
- **Withdrawals:** Withdraw funds (with checks for sufficient balance).
- **Balance Inquiry:** Check your current account balance and account holder name.
- **Interactive CLI:** User-friendly, menu-driven command line interface.

## Usage

1. **Run the program**  
   You need Python installed. Run:
   ```bash
   python BankAccount.py
   ```

2. **Main Menu Options**
   - `[1 access cont]` — Access an existing account by entering your PIN.
   - `[2 create account]` — Create a new account.

3. **Account Actions**
   - `[1 withdrawal]` — Select or enter the amount to withdraw.
   - `[2 sold]` — Display your current balance.
   - `[3 deposit]` — Add money to your account.
   - `[4 exiting and continued manipulation with your account]` — Exit the current session or return to main menu.

## Notes

- Some prompts/messages are in Romanian (e.g., "sold" = balance, "retragerea" = withdrawal).
- All accounts are stored in memory and will be lost after the program ends.
- PINs are randomly generated and must be saved by the user for future access.

## Dependencies

- `colorama` (for colored CLI prompts)
- Standard Python library (`random`)

Install dependencies with:
```bash
pip install colorama
```

## Example

```
[1 access cont]  [2 create account]: 2
Enter Name: Alice
Enter First deposit : 500
account created with pin 1234
[1 withdrawal]: [ 2 sold]: [ 3 deposit]: [ 4 exiting and contined manipulation with your account]:
```

---

*For educational purposes. Not suitable for real banking or storing sensitive data!*