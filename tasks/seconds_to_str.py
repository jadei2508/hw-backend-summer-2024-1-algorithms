__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d:
        return f'{d:02d}d{h:02d}h{m:02d}m{s:02d}s'
    if h:
        return f'{h:02d}h{m:02d}m{s:02d}s'
    if m:
        return f'{m:02d}m{s:02d}s'
    else:
        return f'{s:02d}s'
