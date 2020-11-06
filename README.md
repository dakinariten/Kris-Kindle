# Kris-Kindle
Kris Kindle randomisation script; input list of names with email addresses, and each participant will be emailed their asigned name

Written in Python 3

Basic script with 2 random elements
1.) 1D list passed into function & shuffled
2.) List is iterated through, and validated to ensure no one is assigned their own name
3.) If there is only one name left, and it is the same as the last person, function runs recursively
4.) Returns 2D list; list[0] are the individuals, and list[1] are their assigned names

The first part of this script is getting the list values; this assumes a CSV file with names in first column, and emails in second. Comment out this section if you want to manually code the list & dictionary entries

The second portion of the script deals with emailing; change the variable values to use your own email address. You can decide whether to hardcode your password or not (use input if not).

The message portion can be customised to anything - I recommend changing it to anything else, to ensure no issues with spam filters.
