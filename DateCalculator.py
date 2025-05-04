class DateCalculator:
    """
     Zeller's Congruence formula.
    """

    def __init__(self, year, month, day):
        """
        Initializing with the date components.
        """
        self.original_year = year  # Save the original year
        self.original_month = month  # Save the original month
        self.day = day  # Day of the month

        # Adjusting month and year for January and February
        if month == 1 or month == 2:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def calculate_day_of_week(self):
        """
        Calculating the day of the week using Zeller's Congruence formula.
        """
        # Step 1: Extracting components from the date
        q = self.day  # Day of the month
        m = self.month  # Month (adjusted if needed)
        Y = self.year  # Year (adjusted if needed)
        K = Y % 100  # Year of the century
        J = Y // 100  # Zero-based century

        # Step 2: Apply Zeller's formula
        # h = (q + ⌊13(m + 1) / 5⌋ + K + ⌊K / 4⌋ + ⌊J / 4⌋ + 5J) % 7
        h = (q +
             ((13 * (m + 1)) // 5) +
             K +
             (K // 4) +
             (J // 4) +
             (5 * J)) % 7

        # Step 3: Convert the result to a day name
        # In Zeller's formula, 0 = Saturday, 1 = Sunday, ..., 6 = Friday
        days_of_week = [
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ]

        return days_of_week[h]

    def print_result(self):
        """
        Print the result in a user-friendly format.
        """
        day_name = self.calculate_day_of_week()
        print(f"{self.original_month}/{self.day}/{self.original_year} was a {day_name}.")


# Example usage:
if __name__ == "__main__":
    # what day was September 15, 1589
    calculator = DateCalculator(1589, 9, 15)
    calculator.print_result()
