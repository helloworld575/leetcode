a = """select
    a.Id
from
    weather a,weather b
where
    a.Temperature > b.Temperature and DATEDIFF(a.recorddate,b.recorddate) = 1
    """
    