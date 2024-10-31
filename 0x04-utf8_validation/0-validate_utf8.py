def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    # Masks for the leading bits in each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        if bytes_remaining == 0:
            # Determine the number of bytes for the current character
            mask = 1 << 7
            while mask & byte:
                bytes_remaining += 1
                mask >>= 1

            if bytes_remaining == 0:
                continue

            # UTF-8 encoding is between 1 and 4 bytes only
            if bytes_remaining == 1 or bytes_remaining > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        bytes_remaining -= 1

    return bytes_remaining == 0
