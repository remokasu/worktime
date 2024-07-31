# Define the WorkTime class
from dataclasses import dataclass


@dataclass
class WorkTime:
    hours: int
    minutes: int

    def __post_init__(self):
        # Ensure that minutes are within 0-59 and adjust hours accordingly
        total_minutes = self.hours * 60 + self.minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

    @classmethod
    def from_hhmm(cls, hhmm: int) -> 'WorkTime':
        """Create a WorkTime object from an integer in HHMM format.

        Example:
        >>> WorkTime.from_hhmm(745)
        """
        hours = hhmm // 100
        minutes = hhmm % 100
        return cls(hours, minutes)

    @classmethod
    def from_str(cls, time_str: str) -> 'WorkTime':
        """Create a WorkTime object from a time string in HH:MM format.

        Example:
        >>> WorkTime.from_str('07:45')
        """
        if ':' not in time_str:
            raise ValueError("Time must be in HH:MM format")
        hours, minutes = map(int, time_str.split(':'))
        return cls(hours, minutes)

    def to_minutes(self) -> int:
        """Convert the WorkTime object to total minutes."""
        return self.hours * 60 + self.minutes

    @classmethod
    def from_minutes(cls, total_minutes: int) -> 'WorkTime':
        """Create a WorkTime object from total minutes."""
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return cls(hours, minutes)

    def to_decimal(self) -> float:
        """Convert the WorkTime object to total hours as a decimal."""
        return self.hours + self.minutes / 60

    def __str__(self) -> str:
        """Return the time in HH:MM format."""
        return f"{self.hours:02}:{self.minutes:02}"

    def __add__(self, other: 'WorkTime') -> 'WorkTime':
        """Add two WorkTime objects."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        total_minutes = self.to_minutes() + other.to_minutes()
        return WorkTime.from_minutes(total_minutes)

    def __sub__(self, other: 'WorkTime') -> 'WorkTime':
        """Subtract another WorkTime object from this one."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        total_minutes = self.to_minutes() - other.to_minutes()
        return WorkTime.from_minutes(total_minutes)

    def __mul__(self, factor: int) -> 'WorkTime':
        """Multiply a WorkTime object by an integer factor."""
        if not isinstance(factor, int):
            raise TypeError("Factor must be an integer")
        total_minutes = self.to_minutes() * factor
        return WorkTime.from_minutes(total_minutes)

    def __truediv__(self, divisor: int) -> 'WorkTime':
        """Divide a WorkTime object by an integer divisor."""
        if not isinstance(divisor, int):
            raise TypeError("Divisor must be an integer")
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        total_minutes = self.to_minutes() // divisor
        return WorkTime.from_minutes(total_minutes)

    def __eq__(self, other: 'WorkTime') -> bool:
        """Check if two WorkTime objects are equal."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        return self.to_minutes() == other.to_minutes()

    def __lt__(self, other: 'WorkTime') -> bool:
        """Check if this WorkTime object is less than another."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        return self.to_minutes() < other.to_minutes()

    def __le__(self, other: 'WorkTime') -> bool:
        """Check if this WorkTime object is less than or equal to another."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        return self.to_minutes() <= other.to_minutes()

    def __gt__(self, other: 'WorkTime') -> bool:
        """Check if this WorkTime object is greater than another."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        return self.to_minutes() > other.to_minutes()

    def __ge__(self, other: 'WorkTime') -> bool:
        """Check if this WorkTime object is greater than or equal to another."""
        if not isinstance(other, WorkTime):
            raise TypeError("Operand must be a WorkTime object")
        return self.to_minutes() >= other.to_minutes()

    def __int__(self) -> int:
        """Convert WorkTime object to total minutes as an integer."""
        return self.to_minutes()
    
    def __float__(self) -> float:
        """Convert WorkTime object to total hours as a float."""
        return self.hours + self.minutes / 60


def worktime(hhmm: int | str) -> WorkTime:
    """Create a WorkTime object from an integer or string."""
    if isinstance(hhmm, str):
        return WorkTime.from_str(hhmm)
    else:
        return WorkTime.from_hhmm(hhmm)
