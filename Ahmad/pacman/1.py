def library_fee(days):
    if days > 7:
        extra_days = days-7
        fee = 20 * extra_days