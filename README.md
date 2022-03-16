# Excersice-Payment
Excesrice Payment with txt input

To excecute the programme just excute it on the console with the hour.txt file in the same folder as the source code.
The format of the hour.txt file is the following.
Each line contains the information for one person includeing the name of the person, the day the person works and the time of start and end of each day that person works.
An example of the fortmat would be: person_name=day_in_two_lettersstar_time-end_time 
In the example the values being person_name, day_in_two_letters, start_time, end_time. The only two simbols used are "=" (equal to) and "-" (minus).
At the end of each line it is expected an ENTER.

The app will calculate the amount of USD to pay to each person with the following key.
Prices by the hour:

Monday - Friday
00:01 - 09:00 25 USD/HR
09:01 - 18:00 15 USD/HR
18:01 - 00:00 20 USD/HR

Saturday and Sunday
00:01 - 09:00 30 USD/HR
09:01 - 18:00 20 USD/HR
18:01 - 00:00 25 USD/HR

Two letter day format:

MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday

Name:

All capital letters and only one word (first name).

The only library used is datetime from python itself.

Once ready the hour.txt document, open the console and navigate to the folder with the files in them.
Excecute the command python excersise.py
The result will be shown in the format:
"The amount to pay person_name is: amount_to_pay USD" where person_name and amount_to_pay are the variables.

The proccess wich is excetuted is first open and read the file hours.txt.
Second there are defined the functions to be used later on. Thera are three functions cut_string(string), calculate_hours(initial_time, final_time) and calculate_price(journal_hours, day2let).
In third place there are three variables set names (a list), days  (a list) and name_nbr (an integer).

After this starts the programme excecution.
First it separates the names from the worked hours information. It sabes the names in the names list and the rest in the days list.
Then it goes through the days list. It uses a for loop to do it.
Inside the loop it separates each pearsons days in individual journals while separating the two first letters to from the time worked each day.
It takes the time frame and divides it in starting an ending time.
It calls the calculate_hours() function to get the amount of hours in each time section according to the key for each day.
Then it calls the calculate_price() function to get the amount of USD to pay according to the hours of work in each section according to the information and the key.
It adds the price of each journal in the total_price variable.
It prints the result in the result format.
Finally it adds one to the name_nbr variable to use it as a key to get the names from the list.


