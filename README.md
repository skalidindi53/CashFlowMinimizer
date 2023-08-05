# Cashflow Minimizer 
Cashflow Minimizer is a dynamic financial management tool designed to streamline and simplify the way roommates split rent and utilities. Created to tackle the complexity of shared expenses, this application leverages a specialized algorithm to calculate individual obligations, ensuring a fair and transparent distribution.


## Features
**Dark Theme**: The interface is crafted with a sleek and user-friendly dark theme, providing an attractive and easy-to-navigate experience.

**Flexible Input**: Allows input for 2 to 10 people, accommodating various group sizes.

**Matrix Input**: Users can easily fill a matrix representing the cash flow between the members, with zeros automatically filled for cells where i == j, reflecting that no one owes money to themselves.

## Instructions

### Setting Up Participants
1. Select the number of participants (from 2 to 10) and click the "Submit" button.

### Inputting Transactions
1. A matrix input will appear where you can fill in the amounts that participants owe each other.
2. Cells where `i == j` are automatically filled with zeros, representing that a participant doesn't owe themselves money.
3. Enter the amount owed from participant `i` to participant `j` in the corresponding cell.

### Running the Minimization Algorithm
1. Once the transactions are inputted, click on the "Calculate" button.

### Viewing Results
1. The results will be displayed in a user-friendly format, showing the minimized transactions required to settle all debts.


## Demo
![Updated Demo vide for CFM](https://github.com/skalidindi53/CashFlowMinimizer/assets/94879708/c035f09a-607b-4571-897b-7c190c9a022e)


## Installation
Simply clone this repository and run the main.py file in your code editior.
    
## Code
![image](https://github.com/skalidindi53/CashFlowMinimizer/assets/94879708/19b8518f-c10c-4aaf-baff-22a645d51c47)

